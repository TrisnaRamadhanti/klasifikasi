def findDecision(obj): #obj[0]: peminat_prodi, obj[1]: rerata_ipk, obj[2]: kelulusan, obj[3]: jam_kehadiran_dosen, obj[4]: rerata_nilai_dosen
   if obj[0]>0.0:
      if obj[4]>0.0:
         return 'Berkembang'
      elif obj[4]<=0.0:
         if obj[2]>6:
            if obj[1]>1.521:
               if obj[3]<=0.0:
                  return 'Berkembang'
               else:
                  return 'Berkembang'
            else:
               return 'Berkembang'
         elif obj[2]<=6:
            return 'Belum Berkembang'
         else:
            return 'Belum Berkembang'
      else:
         return 'Belum Berkembang'
   elif obj[0]<=0.0:
      return 'Belum Berkembang'
   else:
      return 'Belum Berkembang'
