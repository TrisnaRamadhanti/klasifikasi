def findDecision(obj): #obj[0]: peminat_prodi, obj[1]: rerata_ipk, obj[2]: kelulusan, obj[3]: jam_kehadiran_dosen, obj[4]: rerata_nilai_dosen
   if obj[3]>0.06059977578475336:
      if obj[1]>0.0:
         if obj[0]<=0.564:
            if obj[2]<=0.4602510460251046:
               if obj[4]>0.0:
                  return 'Berkembang'
               else:
                  return 'Berkembang'
            elif obj[2]>0.4602510460251046:
               return 'Berkembang'
            else:
               return 'Berkembang'
         elif obj[0]>0.564:
            return 'Berkembang'
         else:
            return 'Berkembang'
      elif obj[1]<=0.0:
         if obj[0]<=0.564:
            return 'Belum Berkembang'
         elif obj[0]>0.564:
            if obj[2]<=0.4602510460251046:
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
   elif obj[3]<=0.06059977578475336:
      return 'Belum Berkembang'
   else:
      return 'Belum Berkembang'
