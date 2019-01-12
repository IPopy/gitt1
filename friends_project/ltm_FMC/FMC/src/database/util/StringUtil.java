/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package database.util;

/**
 *
 * @author Administrator
 */
public class StringUtil {
    public static boolean isEmpty(String str){
		if("".equals(str)|| str == null){
			return true;
		}
		return false;
	}

    
}
