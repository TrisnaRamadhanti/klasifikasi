def findDecision(obj): #obj[0]: peminat_prodi, obj[1]: rerata_ipk, obj[2]: kelulusan, obj[3]: jam_kehadiran_dosen, obj[4]: rerata_nilai_dosen
   if obj[1]<=0.6023945675482487:
      if obj[3]<=0.7990690845165382:
         if obj[4]>0.7560321715817694:
            if obj[2]>0.006944444444444444:
               if obj[0]<=0.7518796992481203:
                  return 'Berkembang'
               elif obj[0]>0.7518796992481203:
                  return 'Belum Berkembang'
               else:
                  return 'Belum Berkembang'
            elif obj[2]<=0.006944444444444444:
               return 'Belum Berkembang'
            else:
               return 'Belum Berkembang'
         elif obj[4]<=0.7560321715817694:
            return 'Belum Berkembang'
         else:
            return 'Belum Berkembang'
      elif obj[3]>0.7990690845165382:
         return 'Berkembang'
      else:
         return 'Berkembang'
   elif obj[1]>0.6023945675482487:
      return 'Berkembang'
   else:
      return 'Berkembang'
