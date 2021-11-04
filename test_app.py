from unittest import TestCase

from app import app
app.config["TESTING"]=True
app.config["DEBUG_TB_HOSTS"]=["dont-show-debug-toolbar"]

class RedirectTestCase(TestCase):

    

    def test_homepage(self):

        """Test to see if the inital homepage is being reached"""

        with app.test_client() as client:
            resp=client.get("/")
            self.assertEqual(resp.status_code, 200)

    def test_conversions_list(self):

        """Test to see if the conversions are being pulled and appended to homepage correctly"""

        with app.test_client() as client:
            res= client.post("/converter_page", follow_redirects=True, data={"converting_from": "USD","converting_to": "USD", "amount": "10.55"})
            html=res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<li>US$10.55 is equal to US$10.55</li>", html)