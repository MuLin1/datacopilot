package com.rybin.bank.utils;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.IOException;

public class SqlSessionUtil {
    private static SqlSessionFactoryBuilder sqlSessionFactoryBuilder = null;
    private static SqlSessionFactory sqlSessionFactory = null;

    static {

        try {
            sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
            sqlSessionFactory = sqlSessionFactoryBuilder.
                    build(Resources.getResourceAsReader("mybatis-config.xml"));

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
    //To prevent being created, make constructor private.
    private SqlSessionUtil() {}

    public static SqlSession openSession() {
        return sqlSessionFactory.openSession();
    }
}
