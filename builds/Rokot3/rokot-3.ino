//##############################################
//#           ROKOT  CANSAT  PROJECT           #
//#                   2K17                     #
//##############################################


//##############################################
//#    МЕСТО   ДЛЯ   ПОДКЛЮЧЕНИЯ  БИБЛИОТЕК    #
//##############################################

#include <Wire.h>
#include <MS5611.h>
#include <SPI.h>
#include <SD.h>

//#########################
//#      МЕСТО  ДЛЯ       #
//#      ОБЪЯВЛЕНИЯ       #
//# КОНСТАНТ ДЛЯ ДАТЧИКОВ #
//#########################

#define MPU6050_ACCEL_XOUT_H       0x3B   // R  
#define MPU6050_ACCEL_XOUT_L       0x3C   // R  
#define MPU6050_ACCEL_YOUT_H       0x3D   // R  
#define MPU6050_ACCEL_YOUT_L       0x3E   // R  
#define MPU6050_ACCEL_ZOUT_H       0x3F   // R  
#define MPU6050_ACCEL_ZOUT_L       0x40   // R  
#define MPU6050_I2C_MST_DELAY_CTRL 0x67   // R/W
#define MPU6050_SIGNAL_PATH_RESET  0x68   // R/W
#define MPU6050_MOT_DETECT_CTRL    0x69   // R/W
#define MPU6050_USER_CTRL          0x6A   // R/W
#define MPU6050_PWR_MGMT_1         0x6B   // R/W
#define MPU6050_PWR_MGMT_2         0x6C   // R/W
#define MPU6050_WHO_AM_I           0x75   // R
#define MPU6050_I2C_ADDRESS 0x68


MS5611 ms5611;

union accel_t_gyro_union{
  struct{
    uint8_t x_accel_h; uint8_t x_accel_l; uint8_t y_accel_h; uint8_t y_accel_l; uint8_t z_accel_h; uint8_t z_accel_l;
    uint8_t t_h; uint8_t t_l; uint8_t x_gyro_h; uint8_t x_gyro_l; uint8_t y_gyro_h; uint8_t y_gyro_l;
    uint8_t z_gyro_h; uint8_t z_gyro_l;
  } reg;
  struct {
    int x_accel; int y_accel; int z_accel; int temperature; int x_gyro; int y_gyro; int z_gyro;
  } value;
};

unsigned long last_read_time;

float last_x_angle; float last_y_angle; float last_z_angle; // Акселерометр
float last_gyro_x_angle; float last_gyro_y_angle; float last_gyro_z_angle; // Гироскоп

inline unsigned long get_last_time() { return last_read_time; }
inline float get_last_x_angle() { return last_x_angle; }
inline float get_last_y_angle() { return last_y_angle; }
inline float get_last_z_angle() { return last_z_angle; }
inline float get_last_gyro_x_angle() { return last_gyro_x_angle; }
inline float get_last_gyro_y_angle() { return last_gyro_y_angle; }
inline float get_last_gyro_z_angle() { return last_gyro_z_angle; }

float base_x_accel; float base_y_accel; float base_z_accel; // Акселерометр
float base_x_gyro; float base_y_gyro; float base_z_gyro; // Гироскоп

//##############################################
//#            РАЗЛИЧНЫЕ НАСТРОЙКИ             #
//##############################################

const int chipSelect = 4; //Пин для кард-ридера (стандарт = 4)
const bool sderr = 0; //Выдавать ошибки с SD кардридера 0: нет, 1: да
const bool dCalibrate = 1; //Калибровка датчиков при запуске 0: нет, 1: да
const short baudrate = 9600; // БОД/С
const bool serialOut = 1; //Вывод данных в Serial-порте 0: нет, 1: да
const int dTime = 10; // Теоретическая разница между замерами
#define FILENAME "datalog.txt"
#define HELLO_LABEL "*****************************^-^********************************"


void setup(){ 
  int error; uint8_t c;
  File myFile = SD.open(FILENAME, FILE_WRITE);
  Serial.begin(baudrate); 
  Wire.begin();
  MPU6050_write_reg (MPU6050_PWR_MGMT_1, 0);

  if (dCalibrate){
    calibrate_sensors(); //#КАЛИБРОВКА#
  }
  
  while(!ms5611.begin(MS5611_ULTRA_HIGH_RES)){
    delay(500);
  }
  
  while (!Serial) {
    ; //# НЕМНОГО МАГИИ #//
  }

  if (!SD.begin(chipSelect) and sderr) { 
    Serial.println("CARD FILED OR DON't PRESENTED");
    return;
  } else {
    return;
  }
  
  if (myFile) {
    myFile.println(HELLO_LABEL);
    myFile.close();
  } else {
    if (sderr){
      Serial.println("ERROR OPENING FILE");
    }
  }
  
}

void loop()
{
  int error;
  accel_t_gyro_union accel_t_gyro;
  double realTemperature = ms5611.readTemperature(true);
  long realPressure = ms5611.readPressure(true);
  double realAltitude = ms5611.getAltitude(realPressure);
  File dataFile = SD.open(FILENAME, FILE_WRITE);

  
  // СЧИТЫВАНИЕ СЫРЫХ ДАННЫХ
  error = read_gyro_accel_vals((uint8_t*) &accel_t_gyro);
  
  // ПОЛУЧЕНИЕ ВРЕМЕНИ ЗАМЕРА
  unsigned long t_now = millis();
   
  // КОНВЕРТИРОВАНИЕ ДАННЫХ С ГИРОСКОПА В ГР/С
  float FS_SEL = 131;

  float gyro_x = (accel_t_gyro.value.x_gyro - base_x_gyro)/FS_SEL;
  float gyro_y = (accel_t_gyro.value.y_gyro - base_y_gyro)/FS_SEL;
  float gyro_z = (accel_t_gyro.value.z_gyro - base_z_gyro)/FS_SEL;
  
  // ПОЛУЧЕНИЕ ДАННЫХ УСКОРЕНИЯ
  //float G_CONVERT = 16384;
  float accel_x = accel_t_gyro.value.x_accel;
  float accel_y = accel_t_gyro.value.y_accel;
  float accel_z = accel_t_gyro.value.z_accel;
  
  // ОЧЕНЬ СЛОЖНЫЕ ВЫЧИСЛЕНИЯ, ЛУЧШЕ ЗАКРЫТЬ ГЛАЗКИ
  float RADIANS_TO_DEGREES = 180/3.14159;
  //  float accel_vector_length = sqrt(pow(accel_x,2) + pow(accel_y,2) + pow(accel_z,2));
  float accel_angle_y = atan(-1*accel_x/sqrt(pow(accel_y,2) + pow(accel_z,2)))*RADIANS_TO_DEGREES;
  float accel_angle_x = atan(accel_y/sqrt(pow(accel_x,2) + pow(accel_z,2)))*RADIANS_TO_DEGREES;
  float accel_angle_z = 0;
  
  // ФИЛЬТРОВАНИЕ ДАННЫХ С ГИРОСКОПА
  float dt =(t_now - get_last_time())/1000.0;
  float gyro_angle_x = gyro_x*dt + get_last_x_angle();
  float gyro_angle_y = gyro_y*dt + get_last_y_angle();
  float gyro_angle_z = gyro_z*dt + get_last_z_angle();
  
  // Compute the drifting gyro angles
  float unfiltered_gyro_angle_x = gyro_x*dt + get_last_gyro_x_angle();
  float unfiltered_gyro_angle_y = gyro_y*dt + get_last_gyro_y_angle();
  float unfiltered_gyro_angle_z = gyro_z*dt + get_last_gyro_z_angle();
  
  // ПРИМЕНЕНИЕ ФИЛЬТРА ДЛЯ ВЫЯСНЕНИЯ ИЗМЕНЕНИЯ УГЛА
  // ALPHA ЗАВИСИТ ОТ ЧАСТОТЫ ДИСКРЕТИЗАЦИИ ( БОД/С / 10000)
  float alpha = baudrate / 10000;
  float angle_x = alpha*gyro_angle_x + (1.0 - alpha)*accel_angle_x;
  float angle_y = alpha*gyro_angle_y + (1.0 - alpha)*accel_angle_y;
  float angle_z = gyro_angle_z;  // НУ ВОТ ТАК
  
  // ОБНОВЛЕНИЕ СТАРЫХ ДАННЫХ
  set_last_read_angle_data(t_now, angle_x, angle_y, angle_z, unfiltered_gyro_angle_x, unfiltered_gyro_angle_y, unfiltered_gyro_angle_z);
  
  // ОПЕРАЦИИ ЗАПИСИ И ВЫВОДА
  
  String dataString = "";
  dataString += String(t_now);
  dataString += ", ";
  dataString += String(realTemperature,0);
  dataString += ", ";
  dataString += String(angle_x-1,0);
  dataString += ", ";
  dataString += String(angle_y,0);
  dataString += ", ";
  dataString += String(angle_z,0);
  dataString += ", ";
  dataString += String(gyro_x,0);
  dataString += ", ";
  dataString += String(gyro_y,0);
  dataString += ", ";
  dataString += String(gyro_z,0);
  dataString += ", ";
  dataString += String(realPressure);
  dataString += ", ";
  dataString += String(realAltitude);
  dataString += "\n";

  if (serialOut){
    Serial.print(dataString);
  }
  
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
  } else {
   if (sderr){
      Serial.println("ERROR OPENING FILE");
    }
  }
  
  delay(dTime);
}
