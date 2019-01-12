/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package database.model;

//import database.dao.baseDao;

/**
 *
 * @author Administrator
 */
public class Admin {
    
    private int staffNo;
    private String name;
    private String passWord;
    private String createDate;

    public int getStaffNo() {
        return staffNo;
    }

    public void setStaffNo(int staffNo) {
        this.staffNo = staffNo;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassWord() {
        return passWord;
    }

    public void setPassWord(String passWord) {
        this.passWord = passWord;
    }

    public String getCreateDate() {
        return createDate;
    }

    public void setCreateDate(String createDate) {
        this.createDate = createDate;
    }
    
    
    
}
