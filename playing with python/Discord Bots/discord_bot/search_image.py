from random import choice

class Search:
  def __init__(self):
    self.dog = ["https://i2.wp.com/media.globalnews.ca/videostatic/915/243/UGLYDOG.jpg?w=670&quality=70&strip=all",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1N-zTOHKKZ-Fd-CrReCzn3f34nbaFI6zimw&usqp=CAU",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIFsoIKAagcORcpWecWkLhbzkPYcbdhk5IHA&usqp=CAU"]

    self.cat = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU3K_xpUVi-WuxbM9j6RAHLoPDmEXtcWLaIA&usqp=CAU",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRF2_8v4mQqoTPyM6Ahjq6AXXiRIcqY747xfw&usqp=CAU"]
    self.cringe = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWJeIxmlSzY2k_I2ZcGeTSmXMyRaUHchHwGg&usqp=CAU"]
    self.troll = []
    self.naruto = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe_3FoWjGLdcjiFkAeXXcxFy2emuDFSd5cDg&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8e8TrIShxtAlsgnDYC5EF2YyFlFh1ZoX6tA&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMVzNg3eKzDwiK6j8KQWjEfw6hZbmVsw45kg&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQl2yaGGjvoLbDbhtBGR7roBLJZGwlCOXsKyg&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZoa_gPqiT7SZ8pQNsy6fgraHoRhkHXJLsJQ&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScnT2i6NB_VlcpPC0pP5m6dpQZapVGXlq1Kg&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaMUaD3jZMtQ2CNdthJgekRKa9QFSnh1EfdQ&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROcV2IuAd11Jz4PsZFQrweuXaO2aJ2IE3bdg&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3kueK4WwdHghjucKz6kCE4eSsWK93VEBazg&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRC2GwKRJ7xWSmtFjcZThHo0HdvZUQqPwvroA&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjh0OWDRfnZOP4lrMi1FhL8PQlGWRWzKjpWQ&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRniSZagJNSuT1GDB5q2gPa07S_jSSGN_ggpA&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHNm2WLPXcvJQfxzRAJG991RSMDYWD6sRTIg&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR_-LMBBhJuDRdzSoAUIQtgDTjeXy1U9siDQ&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE5QsPSZ1ZS9mominP-wdXGf-j5Ya1jQSpEA&usqp=CAU",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRzRk0FOLEZL-o6aKzQ-HLgvZB4r5pH627Ug&usqp=CAU",
                   "http://1.bp.blogspot.com/_oaOBSdwJP7k/TCzvGgTEToI/AAAAAAAABAA/8FnLJoNJxrY/s1600/1277997757138.jpg",
                   "http://2.bp.blogspot.com/_oaOBSdwJP7k/TCzvF2-opII/AAAAAAAAA_w/W7WrIC6iLb8/s1600/1277998325622.jpg",
                   "https://pbs.twimg.com/media/Dc8btHGV0AAGcMG.jpg",
                   "https://images4.fanpop.com/image/answers/1777000/1777748_1311278300017.71res_298_169.jpg",
                   "https://narutorealm.files.wordpress.com/2011/10/user-sasuke-uchihas-gurl-xo2.gif",
                   "https://i.pinimg.com/originals/6f/fb/bd/6ffbbd3938131ddd7f07948966772435.jpg",
                   "https://www.animatedtimes.com/wp-content/uploads/2020/04/2-3-1.png",
                   "https://images7.memedroid.com/images/UPLOADED626/5c6e0f59ec53b.jpeg",
                   "https://pm1.narvii.com/7650/b0cf6764911309197c984fd3becb09ff30f09a3cr1-720-885v2_uhq.jpg",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyn4_Tpww_nOjynZuWSQ3KHDoNIUDEECMvyQ&usqp=CAU",
                   "https://media.tenor.com/images/40763ce566e10dcf6d01ee5894fc38fb/tenor.gif",
                   "https://i.pinimg.com/564x/ac/2b/33/ac2b3382706a5e57551be1a515370964.jpg",
                   "https://i.pinimg.com/564x/67/c9/84/67c984cf0fd1908ee279049532670a73.jpg",
                   "https://i.pinimg.com/564x/d6/b8/87/d6b88751cbede198a3c2abfb3e84dd79.jpg",
                   "https://i.pinimg.com/564x/37/01/eb/3701ebffdef223066839483eccc1536d.jpg",
                   "https://i.pinimg.com/564x/a4/1f/4e/a41f4e13c86b9b82654d34ebc5abb481.jpg",
                   "https://cdn141.picsart.com/323500417659201.jpg?type=webp&to=crop&r=256",
                   "https://pm1.narvii.com/7584/8402dc4bfc0671581a29c85718f31c7ecf842266r1-640-360v2_uhq.jpg",
                   "https://i.redd.it/m66fsuy4ua851.jpg",
                   "https://i.pinimg.com/736x/1c/05/14/1c0514ee13e119f22c69cc0cc2743528.jpg"]
    self.repeat = []


  def check_repeat(self, image, command):
    if image in self.repeat:
      self.search_image(command)
    else:
      self.repeat.append(image)
      return image

  def search_image(self, command):
    if command == "do":
      image = choice(self.dog)
      if image in self.repeat:
        self.search_image(command)
      else:
        self.repeat.append(image)
        if image in self.repeat:
          self.search_image(command)
        else:
          self.repeat.append(image)
          return image
    elif command == "naruto":
      image = choice(self.naruto)
      if image in self.repeat:
        self.search_image(command)
      else:
        self.repeat.append(image)
        return image
    elif command == "cat":
      image = choice(self.cat)
      if image in self.repeat:
        self.search_image(command)
      else:
        self.repeat.append(image)
        return image
    elif command == "troll":
      image = choice(self.troll)
      if image in self.repeat:
        self.search_image(command)
      else:
        self.repeat.append(image)
        return image