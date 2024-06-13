package com.rybin.bank.web;

import com.rybin.bank.mapper.CarMapper;
import com.rybin.bank.pojo.Car;
import com.rybin.bank.utils.SqlSessionUtil;
import org.apache.ibatis.session.SqlSession;
import org.junit.Test;

import java.util.ArrayList;

public class test {
    @Test
    public void test() throws Exception {
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        System.out.println(mapper.selectById(1));
    }

    @Test
    public void test1() throws Exception {
        SqlSession sqlSession = SqlSessionUtil.openSession();
        CarMapper mapper = sqlSession.getMapper(CarMapper.class);
        System.out.println(mapper.insertCar(new Car(null, "1010", "丰田", 30, "2020-10-10", "燃油che")));
    }
}
