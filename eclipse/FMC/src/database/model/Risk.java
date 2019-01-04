/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package database.model;

/**
 *
 * @author Administrator
 */
public class Risk {
    
    private String selectedDate;
    private int PredictedPatient;
    private int ExpectedAdmittedNumber;
    private double NewArrvialRate;
    private int Electives;
    private int MidnightOccupancy;
    private int ExpectedDischargeNumber;
    private double DischargeRate;
    private int Threshold;
    private double Risk1;
    private int Threshold2;
    private int AdmitMore;
    private double NewArrivalRate2;
    private int DischargeMore;
    private double DischargeRate2;
    private  double Risk2;

    public String getSelectedDate() {
        return selectedDate;
    }

    public void setSelectedDate(String selectedDate) {
        this.selectedDate = selectedDate;
    }

    

    public int getPredictedPatient() {
        return PredictedPatient;
    }

    public void setPredictedPatient(int PredictedPatient) {
        this.PredictedPatient = PredictedPatient;
    }

    public int getExpectedAdmittedNumber() {
        return ExpectedAdmittedNumber;
    }

    public void setExpectedAdmittedNumber(int ExpectedAdmittedNumber) {
        this.ExpectedAdmittedNumber = ExpectedAdmittedNumber;
    }

    public double getNewArrvialRate() {
        return NewArrvialRate;
    }

    public void setNewArrvialRate(double NewArrvialRate) {
        this.NewArrvialRate = NewArrvialRate;
    }

    public int getElectives() {
        return Electives;
    }

    public void setElectives(int Electives) {
        this.Electives = Electives;
    }

    public int getMidnightOccupancy() {
        return MidnightOccupancy;
    }

    public void setMidnightOccupancy(int MidnightOccupancy) {
        this.MidnightOccupancy = MidnightOccupancy;
    }

    public int getExpectedDischargeNumber() {
        return ExpectedDischargeNumber;
    }

    public void setExpectedDischargeNumber(int ExpectedDischargeNumber) {
        this.ExpectedDischargeNumber = ExpectedDischargeNumber;
    }

    public double getDischargeRate() {
        return DischargeRate;
    }

    public void setDischargeRate(double DischargeRate) {
        this.DischargeRate = DischargeRate;
    }

    public int getThreshold() {
        return Threshold;
    }

    public void setThreshold(int Threshold) {
        this.Threshold = Threshold;
    }

    public double getRisk1() {
        return Risk1;
    }

    public void setRisk1(double Risk1) {
        this.Risk1 = Risk1;
    }

    public int getThreshold2() {
        return Threshold2;
    }

    public void setThreshold2(int Threshold2) {
        this.Threshold2 = Threshold2;
    }

    public int getAdmitMore() {
        return AdmitMore;
    }

    public void setAdmitMore(int AdmitMore) {
        this.AdmitMore = AdmitMore;
    }

    public double getNewArrivalRate2() {
        return NewArrivalRate2;
    }

    public void setNewArrivalRate2(double NewArrivalRate2) {
        this.NewArrivalRate2 = NewArrivalRate2;
    }

    public int getDischargeMore() {
        return DischargeMore;
    }

    public void setDischargeMore(int DischargeMore) {
        this.DischargeMore = DischargeMore;
    }

    public double getDischargeRate2() {
        return DischargeRate2;
    }

    public void setDischargeRate2(double DischargeRate2) {
        this.DischargeRate2 = DischargeRate2;
    }

    public double getRisk2() {
        return Risk2;
    }

    public void setRisk2(double Risk2) {
        this.Risk2 = Risk2;
    }
    
    
    
}
