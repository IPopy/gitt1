/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package database.dao;

import database.model.Risk;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Administrator
 */
public class DateDao extends baseDao {

    /*public Risk getDateInfo() {
        String sql = "select * from RiskAnalysis where Date=selectedDate";
        Risk oTemp = null;
       // String ExpectedAdmittedNumber=null;
        try {
            PreparedStatement prst = con.prepareStatement(sql); // 把sql 语句传给数据操作对象
            prst.setString(1, admin.getName());
            prst.setInt(1, oTemp.getAdmitMore());
            prst.setInt(2, oTemp.getDischargeMore());
            prst.setInt(3, oTemp.getElectives());
            prst.setInt(4, oTemp.getExpectedAdmittedNumber());
            prst.setInt(5, oTemp.getMidnightOccupancy());
            prst.setInt(6, oTemp.getPredictedPatient());
            prst.setInt(7, oTemp.getThreshold());
            prst.setInt(8, oTemp.getThreshold2());
            prst.setDouble(9, oTemp.getDischargeRate());
            prst.setDouble(10, oTemp.getDischargeRate2());
            prst.setDouble(11, oTemp.getNewArrvialRate());
            prst.setDouble(12, oTemp.getNewArrivalRate2());
            prst.setDouble(13, oTemp.getRisk1());
            prst.setDouble(14, oTemp.getRisk2());
            prst.setInt(15, oTemp.getExpectedDischargeNumber());
            ResultSet executeQuery = prst.executeQuery();
            if (executeQuery.next()) {
                oTemp = new Risk();
                oTemp.setExpectedAdmittedNumber(executeQuery.getInt("ExpectedAdmittedNumber"));
                oTemp.setExpectedDischargeNumber(executeQuery.getInt("ExpectedDischargeNumber"));
            }
        } catch (SQLException ex) {
            //Logger.getLogger(DateDao.class.getName()).log(Level.SEVERE, null, ex);
        }
        try {
            con.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return oTemp;
    }
*/
    public Risk getDateInfo() {
        String sql = "select * from riskanalysis where Date=selectedDate";
        Risk oTemp = null;
       // String ExpectedAdmittedNumber=null;
        try {
            PreparedStatement prst = con.prepareStatement(sql); // 把sql 语句传给数据操作对象
            ResultSet executeQuery = prst.executeQuery();
            if (executeQuery.next()) {
                oTemp = new Risk();
                oTemp.setExpectedAdmittedNumber(executeQuery.getInt("ExpectedAdmittedNumber"));
                oTemp.setExpectedDischargeNumber(executeQuery.getInt("ExpectedDischargeNumber"));
                oTemp.setAdmitMore(executeQuery.getInt("AdmitMore"));
                oTemp.setDischargeMore(executeQuery.getInt("DischargeMore"));
                oTemp.setDischargeRate(executeQuery.getDouble("DischargeRate"));
                oTemp.setDischargeRate2(executeQuery.getDouble("DischargeRate2"));
                oTemp.setElectives(executeQuery.getInt("Electives"));
                oTemp.setMidnightOccupancy(executeQuery.getInt("Occupancy"));
                oTemp.setNewArrivalRate2(executeQuery.getDouble("NewArrivalRate2"));
                oTemp.setNewArrvialRate(executeQuery.getDouble("NewArrivalRate"));
                oTemp.setPredictedPatient(executeQuery.getInt("PredictedPatient"));
                oTemp.setRisk1(executeQuery.getDouble("Risk1"));
                oTemp.setRisk2(executeQuery.getDouble("Risk2"));
                oTemp.setSelectedDate(executeQuery.getString("SelectedDate"));
                oTemp.setThreshold(executeQuery.getInt("Threshold"));
                oTemp.setThreshold2(executeQuery.getInt("Threshold2"));
            }
        } catch (SQLException ex) {
            //Logger.getLogger(DateDao.class.getName()).log(Level.SEVERE, null, ex);
        }
        try {
            con.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return oTemp;
    }
}
