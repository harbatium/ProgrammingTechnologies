using System;
using System.Runtime.InteropServices;

namespace Lab1
{
    internal class Lab1
    {
        public static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            a *= Convert.ToInt32(Math.Pow(3, 2));
            int[] massiv = new int[a];
            Random rnd = new Random();
            for (int i = 0; i < a; i++)
            {
                massiv[i]= rnd.Next();
            }
            Console.WriteLine("{0}", string.Join(" ", massiv));
        }   
    }
}