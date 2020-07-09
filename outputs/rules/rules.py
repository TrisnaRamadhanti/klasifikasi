def findDecision(obj): #obj[0]: peminat_prodi, obj[1]: rerata_ipk, obj[2]: kelulusan, obj[3]: jam_kehadiran_dosen, obj[4]: rerata_nilai_dosen
   if obj[1]<=3.371:
      if obj[3]<=16.0:
         if obj[4]>2.82:
            if obj[2]>1:
               if obj[0]<=1.0:
                  return 'Berkembang'
               elif obj[0]>1.0:
                  return 'Belum Berkembang'
               else:
                  return 'Belum Berkembang'
            elif obj[2]<=1:
               return 'Belum Berkembang'
            else:
               return 'Belum Berkembang'
         elif obj[4]<=2.82:
            return 'Belum Berkembang'
         else:
            return 'Belum Berkembang'
      elif obj[3]>16.0:
         return 'Berkembang'
      else:
         return 'Berkembang'
   elif obj[1]>3.371:
      return 'Berkembang'
   else:
      return 'Berkembang'
