package com.rybin.bank.mapper;

import com.rybin.bank.pojo.Car;
import org.apache.ibatis.annotations.Param;

import java.util.List;

public interface CarMapper {
    // annotation 'Param' let MyBatis know parameters` names(used in mapper.xml),
    // HAVE NOTHING TO DO WITH SETTING OF CAMELxxx.
    public Car selectMultiple(@Param("id") long id, @Param("carNum") String carNum, @Param("guidePrice") double guidePrice) ;
    //public Car selectMultiple(long id, String carNum, double guidePrice) ;

    public Car selectById(@Param("id") long id) ;

    public int insertCar(Car car) ;

    public int insertBatch(@Param("cars") List<Car> cars) ;
}
