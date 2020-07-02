package tests;

import base.GalenTestBase;
import org.testng.annotations.Test;

import java.io.IOException;


public class WelcomePageTest extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void welcomePage_shouldLookGood_onDevice(TestDevice device) throws IOException {
        load("/");
        checkLayout("/specs/mainPage.spec", device.getTags());
    }

//    @Test(dataProvider = "devices")
//    public void loginPage_shouldLookGood_onDevice(TestDevice device) throws IOException {
//        load("/");
//        GalenPageDump galenPageDump = new GalenPageDump("mainPageTechnokratos");
//        galenPageDump.dumpPage(,"resources/" , "resources/");
//    }

}
