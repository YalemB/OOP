import time
class Utiles():


    def insert_data_to_form(self,form_element, data_fields):
        index = 0
        for i in form_element:
            if i.tag_name == "input" or i.tag_name == "textarea":
                if index < 3:
                    i.send_keys(data_fields[index])
                    index += 1
                    time.sleep(2)


    def is_send_message_button_enabled(self,form_element):
        button = form_element[-1]
        return button.is_enabled()

    def send_message_button(self,form_element,
                            data_fields,
                            expected_is_enabled):
        self.insert_data_to_form(form_element, data_fields)
        is_enabled = self.is_send_message_button_enabled(form_element)

        assert is_enabled == expected_is_enabled