print('''
========================================================
========================================================
========================================================
                                                       
***********  * * * * * * *    * * * * * * * *    *    
          *  *                *                 
          *  *                *                  *
          *  *                *                  *
          *  *                *                  *
          *  *                *                  *
          *  * * * * * * *    *     * * * * *    *   
          *  *                *     *       *    *
          *  *                *             *    * 
          *  *                *             *    *
       *     *                *             *    *
     *       *                *             *    *
   *         *                *             *    *
*            * * * * * * *    * * * * * * * *    *
========================================================
========================================================
========================================================
''')

tabungan_dict = {
     0:{
          'nama':'Aradea',
          'harga laptop':'500 USD',
          'tabungan minggu ke-1':125,
          'tabungan minggu ke-2':100,
          'tabungan minggu ke-3':0,
          'tabungan minggu ke-4':0,
     },
     1:{
          'nama':'Safwan',
          'harga laptop':'300 USD',
          'tabungan minggu ke-1':50,
          'tabungan minggu ke-2':150,
          'tabungan minggu ke-3':0,
          'tabungan minggu ke-4':0,
     },
     2:{
          'nama':'Fatima',
          'harga laptop':'250 USD',
          'tabungan minggu ke-1':75,
          'tabungan minggu ke-2':55,
          'tabungan minggu ke-3':110,
          'tabungan minggu ke-4':0,
     }
}


def main():
     print('\nOutput Dictionary\n')
     print('='*100)
     # Memanggil fungsi rerata
     rerata()
     print(tabungan_dict,'\n')

     print('='*100,'\n')
     # Memanggil fungsi tampil terbanyak
     tampil_terbanyak()




def rerata():
     # mengubah dictionary menjadi list
     tabungan_list = list(tabungan_dict)

     # Mengambil nilai dari dictionary
     nilai = tabungan_dict.values()
     get_nilai = list(nilai)
     
     # Mencari nama mahasiswa yang sama 
     for i in  tabungan_list:
               total = get_nilai[i]['tabungan minggu ke-1']+get_nilai[i]['tabungan minggu ke-2']+get_nilai[i]['tabungan minggu ke-3']+get_nilai[i]['tabungan minggu ke-4']
               avg = total/4
               tabungan_dict[i]['Rata-rata'] = avg
               
     
     return avg

def tampil_terbanyak():
     # mengubah dictionary menjadi list
     tabungan_list = list(tabungan_dict)

     # Mengambil nilai dari dictionary
     nilai = tabungan_dict.values()
     get_nilai = list(nilai)
     
     # Mencari nama mahasiswa yang sama 
     for i in  tabungan_list:
          max = 0
          total = get_nilai[i]['tabungan minggu ke-1']+get_nilai[i]['tabungan minggu ke-2']+get_nilai[i]['tabungan minggu ke-3']+get_nilai[i]['tabungan minggu ke-4']
          if total > max :
               max = total    
     print(f'Tabungan Mahasiswa terbanyak dalam empat minggu adalah milik {get_nilai[i]["nama"]} sebesar {max} USD ') 
     return max

     
if __name__ == "__main__" :
     main()
