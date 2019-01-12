/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package database.dao;

import java.sql.Connection;
import database.util.DbUtil;
import java.sql.SQLException;


/**
 *
 * @author Administrator
 */

public class baseDao {
    public Connection con = new DbUtil().getCon();
    
    public void closeDao(){
		try {
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
