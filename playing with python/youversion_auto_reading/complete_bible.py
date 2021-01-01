#Import these modules to be using
from selenium import webdriver
from time import sleep


class Complete:
	def __init__(self):
		self.service = webdriver.chrome.service.Service("/home/ianchu0317/complete_bible/chromedriver")
		self.driver = webdriver.Chrome(service=self.service)

	def sign_in(self):
		self.driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=117344358296665&kid_directed_site=0&app_id=117344358296665&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fapp_id%3D117344358296665%26cbt%3D1609505371246%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3bbf013bf49548%2526domain%253Dmy.bible.com%2526origin%253Dhttps%25253A%25252F%25252Fmy.bible.com%25252Ff1e3c027be55c34%2526relation%253Dopener%26client_id%3D117344358296665%26display%3Dpopup%26domain%3Dmy.bible.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmy.bible.com%252Fsign-in%26locale%3Den_US%26logger_id%3Df2516cafb151588%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2a6078b8fb3958%2526domain%253Dmy.bible.com%2526origin%253Dhttps%25253A%25252F%25252Fmy.bible.com%25252Ff1e3c027be55c34%2526relation%253Dopener%2526frame%253Df130b35e827d42c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cpublish_to_groups%252Cgroups_access_member_info%26sdk%3Djoey%26version%3Dv3.1%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2a6078b8fb3958%26domain%3Dmy.bible.com%26origin%3Dhttps%253A%252F%252Fmy.bible.com%252Ff1e3c027be55c34%26relation%3Dopener%26frame%3Df130b35e827d42c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=en_US&pl_dbl=0")		
		self.driver.find_element_by_xpath("//*[@id='email']").send_keys(str(credentials[0]))
		self.driver.find_element_by_xpath("//*[@id='pass']").send_keys(str(credentials[1]))
		self.driver.find_element_by_xpath("//*[@id='u_0_0']").click()
		sleep(6)
		self.driver.get("https://www.bible.com/")
		sleep(4)
		self.driver.find_element_by_xpath("//*[@id='react-app-Header']/div/div/div/div[1]/div[3]/div/div/a[1]").click()
		sleep(3)
		self.driver.find_element_by_xpath("//*[@id='facebookSigninButton']/span[2]").click()
		sleep(12)
		self.enter_plan()

	def enter_plan(self):
		self.driver.find_element_by_xpath("//*[@id='react-app-Header']/div/div/div/div[1]/div[1]/div/div/div[3]/a").click()
		sleep(13)
		self.driver.find_element_by_xpath("//*[@id='react-app-PlanDiscovery']/div/div[2]/div[2]/div[1]/div/ul/div[1]/div[1]/div/div[2]/a/h3").click()
		sleep(5)
		self.read_plan()

	def read_plan(self):
		for days in range(360):
			#try:
			self.driver.find_element_by_xpath("//*[@id='react-app-PlanDiscovery']/div/div/div[4]/div[3]/div/div/div/a").click()
			sleep(6)
			for item in range(8+1):
					try:
						bot.driver.find_element_by_xpath("//*[@id='react-app-PlanDiscovery']/div/div/div[1]/div[2]/div/div/div/div[3]/div/a/div").click()
						sleep(2.5)
					except: 
						pass
			self.driver.find_element_by_xpath("//*[@id='react-app-PlanDiscovery']/div/div[2]/div[2]/div[1]/a").click()
			sleep(4)
			#except:
				#pass

if __name__ == "__main__":
	with open("credentials.txt", "r") as file:
		credentials = file.read().split()
	bot = Complete()
	bot.sign_in()
