def findDecision(obj): #obj[0]: peminat_prodi, obj[1]: rerata_ipk, obj[2]: kelulusan, obj[3]: jam_kehadiran_dosen, obj[4]: rerata_nilai_dosen
   if obj[3]>1.0811:
      if obj[1]>0.0:
         if obj[0]<=0.705:
            if obj[2]<=110:
               if obj[4]>0.0:
                  return 'Berkembang'
               else:
                  return 'Berkembang'
            elif obj[2]>110:
               return 'Berkembang'
            else:
               return 'Berkembang'
         elif obj[0]>0.705:
            return 'Berkembang'
         else:
            return 'Berkembang'
      elif obj[1]<=0.0:
         if obj[0]<=0.705:
            return 'Belum Berkembang'
         elif obj[0]>0.705:
            if obj[2]<=110:
               if obj[4]>0.0:
                  return 'Belum Berkembang'
               else:
                  return 'Belum Berkembang'
            else:
               return 'Belum Berkembang'
         else:
            return 'Belum Berkembang'
      else:
         return 'Belum Berkembang'
   elif obj[3]<=1.0811:
      return 'Belum Berkembang'
   else:
      return 'Belum Berkembang'
