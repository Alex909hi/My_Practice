using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
  

namespace Rextester
{
    
   public static class Extensions
 {
    // этот метод делает 1-ые буквы слов заглавными,
     //проверяет на strLen и сортирует
   public static string First_up_and_strLen(this string str, int num)
   {
     str = str.ToLower();       
     string[] words = str.Split(new string[] { ", " },
     StringSplitOptions.RemoveEmptyEntries);
     string format_str = "";
     for(int i = 0; i < words.Length; i++)
            {
              if(words[i].Length >= num)
              {
                  words[i] = words[i][0].ToString().ToUpper() + words[i].Substring(1);
                  format_str += words[i] +", ";
              }
            }    
       //вызываем метод Sort
        return Sort(format_str);
   }
       
       // сортируем строку
    public static string Sort(string format_str )
    {
      string[] orderwords = format_str.Split(new string[] { ", " },StringSplitOptions.RemoveEmptyEntries);
       var format_orderwords = orderwords.OrderBy(p=>p); 
       string all_right = "";
       foreach (var p in format_orderwords)
        all_right += Convert.ToString(p + ", ");
         return all_right;
    }
       
       //К каждому месяцу добавляет порядковый номер 
   public static string Months_num(this string str)
       {
        var months = new Dictionary<string, int>()
          {
              {"Январь", 1},
              {"Февраль", 2},
              {"Март", 3},
              {"Апрель", 4},
              {"Май", 5},
              {"Июнь", 6},
              {"Июль", 7},
              {"Август", 8},
              {"Сентябрь", 9},
              {"Октябрь", 10},
              {"Ноябрь", 11},
              {"Декабрь", 12}
           };
       
        foreach( var month in months)
         {
            str = str.Replace(month.Key, $"{month.Key}({months[month.Key]})");
         }
       return str;
       }
 }
  
	public class Program
	{
		public static void Main(string[] args)
		{
           Console.WriteLine("Введите строку:");
        //   string str = Convert.ToString(Console.ReadLine());
		   string str = "Январь, феВраль, МАРТ, «Высо9тныЙ дом», ВА8Р, раЛ??";
           str = Regex.Replace(str,@"[^а-яА-Я, ]+", "") ; 
           Console.WriteLine("Введите число strLen:");
           int num =Convert.ToInt32( Console.ReadLine()); 
           //int num = 3;
           str = str.First_up_and_strLen(num);
           str = str.Months_num();
           Console.WriteLine(str);     
		}
	}
}