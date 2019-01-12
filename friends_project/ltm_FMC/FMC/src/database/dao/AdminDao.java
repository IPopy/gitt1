/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package database.dao;

import database.model.Admin;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 *
 * @author Administrator
 */
public class AdminDao extends baseDao {

    public Admin login(Admin admin) {
        String sql = "select * from admin where name=? and password=?";
        Admin adminRst = null;
        try {
            PreparedStatement prst = con.prepareStatement(sql); // 把sql 语句传给数据操作对象
            prst.setString(1, admin.getName());
            prst.setString(2, admin.getPassWord());
            ResultSet executeQuery = prst.executeQuery();
            if (executeQuery.next()) {
                adminRst = new Admin();
                adminRst.setStaffNo(executeQuery.getInt("staffNo"));
                adminRst.setName(executeQuery.getString("name"));
                adminRst.setPassWord(executeQuery.getString("passWord"));
                adminRst.setCreateDate(executeQuery.getString("createDate"));
            }
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            con.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return adminRst;
    }

    public String ChangeUserName(Admin admin, String newUserName) {
        String sql = "select * from admin where StaffNo=? and name=?";
        PreparedStatement prst = null;
        int staffNo = 0;
        try {
            prst = con.prepareStatement(sql);
            prst.setInt(1, admin.getStaffNo());
            prst.setString(2, admin.getName());
            ResultSet executeQuery = prst.executeQuery();
            if (!executeQuery.next()) {
                String retString = "previous user name is wrong！";
                return retString;
            }
            staffNo = executeQuery.getInt("staffNo");
        } catch (SQLException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }//把sql语句传给数据库操作对象
        String retString = "Failed to change user name";
        String sqlString = "update admin set name = ? where staffNo = ?";
        try {
            prst = con.prepareStatement(sqlString);
            prst.setString(1, newUserName);
            prst.setInt(2, staffNo);
            int rst = prst.executeUpdate();
            if (rst > 0) {
                retString = "Successfully chnage user name！";
            }
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }//把sql语句传给数据库操作对象
        return retString;
    }

    public String ChangePassWord(Admin admin, String newPassWord) {
        String sql = "select * from admin where StaffNo=? and passWord=?";
        PreparedStatement prst = null;
        int staffNo = 0;
        try {
            prst = con.prepareStatement(sql);
            prst.setInt(1, admin.getStaffNo());
            prst.setString(2, admin.getPassWord());
            ResultSet executeQuery = prst.executeQuery();
            if (!executeQuery.next()) {
                String retString = "Old password is wrong！";
                return retString;
            }
            staffNo = executeQuery.getInt("staffNo");
        } catch (SQLException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }//把sql语句传给数据库操作对象
        String retString = "Failed to change password";
        String sqlString = "update admin set passWord = ? where staffNo = ?";
        try {
            prst = con.prepareStatement(sqlString);
            prst.setString(1, newPassWord);
            prst.setInt(2, staffNo);
            int rst = prst.executeUpdate();
            if (rst > 0) {
                retString = "Successfully chnage password！";
            }
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }//把sql语句传给数据库操作对象
        return retString;

    }

}
