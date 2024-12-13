from Page_Object.Additional_Informations_Page import AdditionalInfo
import time


class Additional_Information(AdditionalInfo):
    def select_Option(self, additional_type,Text_Additional_field):

        if additional_type == 1:
            Google = self.driver.find_element(*self.google)
            Google.click()

        elif additional_type == 2:
            Facebook = self.driver.find_element(*self.facebook)
            Facebook.click()

        elif additional_type == 3:
            Instagram = self.driver.find_element(*self.instagram)
            Instagram.click()

        elif additional_type == 4:
            Reffered = self.driver.find_element(*self.referred)
            Reffered.click()

        elif additional_type == 5:
            Company = self.driver.find_element(*self.company)
            Company.click()

        elif additional_type == 6:
            Agreement = self.driver.find_element(*self.agreement)
            Agreement.click()

        elif additional_type == 7:
            University = self.driver.find_element(*self.university)
            University.click()

        elif additional_type == 8:
            Speech = self.driver.find_element(*self.speech)
            Speech.click()

        else:
            Webinar = self.driver.find_element(*self.webinar)
            Webinar.click()




        try:
            text_field = self.driver.find_element(*self.Text_Bar)
            text_field.click()
            print('*****************************************\t')
            print('Web element found\t')
            print('*****************************************')
            text_field.send_keys(Text_Additional_field)

        except:
            print("No text field found")

        time.sleep(2)

        Finish_bttn = self.driver.find_element(*self.Finish_button)
        Finish_bttn.click()
        time.sleep(2)







