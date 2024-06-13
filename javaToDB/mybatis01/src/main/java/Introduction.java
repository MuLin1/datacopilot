import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.InputStream;

public class Introduction {
    public static void main(String[] args) throws Exception {
        SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();

        InputStream is = Resources.getResourceAsStream("mybatis-config.xml");

        // build() needs an InputStream object pointing to config file.
        SqlSessionFactory sqlSessionFactory = sqlSessionFactoryBuilder.build(is);

        SqlSession sqlSession = sqlSessionFactory.openSession();

        // Use session to execute sql statement.
        int count = sqlSession.insert("insertCar");

        // Notice that MyBatis won`t automatically submit, AKA transaction is available by default.
        sqlSession.commit();

    }
}
