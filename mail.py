# Cleaned by TheZ
import os
import platform
import tkinter as tk
import threading
import time
import random
import logging
from tkinter import messagebox
from datetime import datetime
from math import sin
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import Select
import customtkinter as ctk
import requests
import dns.resolver
from fake_useragent import UserAgent
from email_validator import validate_email, EmailNotValidError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
THEME = {
    "bg_dark": "#0D0D0D",
    "bg_light": "#1A1A1A",
    "accent": "#FF0000",
    "accent_hover": "#CC0000",
    "text": "#FFFFFF",
    "success": "#00FF00",
    "error": "#FF0000",
    "button_hover": "#FF3333",
    "progress_bg": "#333333",
    "highlight": "#FF3366",
}
BROWSER_PROFILES = [
    {
        "viewport": "1920,1080",
        "platform": "Windows",
        "vendor": "Google Inc.",
        "renderer": "ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0)",
    },
    {
        "viewport": "1366,768",
        "platform": "Linux",
        "vendor": "Google Inc.",
        "renderer": "Mesa DRI Intel(R) HD Graphics 520 (Skylake GT2)",
    },
    {
        "viewport": "2560,1440",
        "platform": "MacIntel",
        "vendor": "Apple Inc.",
        "renderer": "Apple GPU",
    },
]
PLATFORM = [
    {
        "name": "Epic Games",
        "url": "https://www.epicgames.com/id/register",
        "email_id": "email",
        "success_patterns": ["verification", "confirm", "welcome"],
    },
    {
        "name": "Steam",
        "url": "https://store.steampowered.com/join",
        "email_id": "email",
        "success_patterns": ["check your email", "verify"],
    },
    {
        "name": "Riot Games",
        "url": "https://auth.riotgames.com/login",
        "email_id": "riot-signup-email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Ubisoft",
        "url": "https://account.ubisoft.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Battle.net",
        "url": "https://account.battle.net/creation",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "GOG",
        "url": "https://www.gog.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "welcome"],
    },
    {
        "name": "Xbox",
        "url": "https://signup.live.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "welcome"],
    },
    {
        "name": "PlayStation",
        "url": "https://id.sonyentertainmentnetwork.com/create_account/",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Nintendo",
        "url": "https://accounts.nintendo.com/register",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "EA",
        "url": "https://www.ea.com/register",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Rockstar Games",
        "url": "https://socialclub.rockstargames.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "welcome"],
    },
    {
        "name": "Bethesda",
        "url": "https://bethesda.net/signup",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Square Enix",
        "url": "https://membership.square-enix.com/register",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Minecraft",
        "url": "https://www.minecraft.net/signup",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Warframe",
        "url": "https://www.warframe.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Path of Exile",
        "url": "https://www.pathofexile.com/register",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Guild Wars 2",
        "url": "https://account.arena.net/register",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Black Desert",
        "url": "https://www.naeu.playblackdesert.com/Register",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Lost Ark",
        "url": "https://www.playlostark.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Star Citizen",
        "url": "https://robertsspaceindustries.com/enlist",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Albion Online",
        "url": "https://albiononline.com/register",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Genshin Impact",
        "url": "https://genshin.hoyoverse.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Honkai Impact",
        "url": "https://honkaiimpact3.mihoyo.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Wargaming",
        "url": "https://wargaming.net/registration",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Gaijin",
        "url": "https://login.gaijin.net/register",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Perfect World",
        "url": "https://www.perfectworld.com/register",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "Nexon",
        "url": "https://www.nexon.com/account/signup",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Gameforge",
        "url": "https://gameforge.com/signup",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
    {
        "name": "My.Games",
        "url": "https://account.my.games/signup",
        "email_id": "email",
        "success_patterns": ["verify", "confirm"],
    },
    {
        "name": "Innova",
        "url": "https://passport.innova.com/registration",
        "email_id": "email",
        "success_patterns": ["verify", "check"],
    },
]
class ModernEmailTester(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Email Validator - TheZ (Bugged)")
        self.geometry("1200x800")
        self.resizable(False, False)
        self.iconbitmap("icon.ico")
        self.configure(fg_color=THEME["bg_dark"])
        self.running = False
        self.working_sites = []
        self.total_successes = 0
        self.completed_tests = 0
        self.total_tests = len(PLATFORM)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.setup_ui()
        self.start_animations()
        self.auto_kill_enabled = True
        self.start_auto_kill()
    def start_animations(self):
        self.animate_counter = 0
        self.pulse_animation()
    def pulse_animation(self):
        self.animate_counter += 1
        pulse_color = f"#{abs(int(sin(self.animate_counter/20) * 20 + 235)):02x}0000"
        self.start_button.configure(fg_color=pulse_color)
        self.after(50, self.pulse_animation)
    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.create_header_frame()
        self.create_main_frame()  # This already creates your results area
        self.create_status_frame()
    def create_header_frame(self):
        header = ctk.CTkFrame(self, fg_color=THEME["bg_light"], height=100)
        header.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        title = ctk.CTkLabel(
            header,
            text="EMAIL VALIDATOR - TheZ",
            font=("Roboto", 32, "bold"),
            text_color=THEME["accent"],
        )
        title.pack(pady=10)
        input_frame = ctk.CTkFrame(header, fg_color="transparent")
        input_frame.pack(fill="x", padx=20, pady=5)
        self.email_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter email to validate...",
            width=400,
            height=45,
            border_color=THEME["accent"],
            fg_color=THEME["bg_light"],
            text_color=THEME["text"],
        )
        self.email_entry.pack(side="left", padx=(0, 10))
        self.start_button = ctk.CTkButton(
            input_frame,
            text="START VALIDATION",
            command=self.start_validation,
            fg_color=THEME["accent"],
            hover_color=THEME["button_hover"],
            height=45,
            font=("Roboto", 14, "bold"),
        )
        self.start_button.pack(side="left", padx=5)
        self.stop_button = ctk.CTkButton(
            input_frame,
            text="STOP",
            command=self.stop_validation,
            fg_color="#666666",
            hover_color="#444444",
            height=45,
            font=("Roboto", 14, "bold"),
            state="disabled",
        )
        self.stop_button.pack(side="left", padx=5)
        self.force_button = ctk.CTkButton(
            input_frame,
            text="FORCE RESULTS",
            command=self.force_results,
            fg_color="#ff6b00",
            hover_color="#cc5500",
            height=45,
            font=("Roboto", 14, "bold"),
        )
        self.force_button.pack(side="left", padx=5)
        self.kill_button = ctk.CTkButton(
            input_frame,
            text="AUTO-KILL ENABLED",
            command=self.toggle_auto_kill,
            fg_color="#ff0000",
            hover_color="#cc0000",
            height=45,
            font=("Roboto", 14, "bold"),
        )
        self.kill_button.pack(side="left", padx=5)
        self.auto_kill_enabled = True
        self.start_auto_kill()
    def force_results(self):
        """Nuclear option to force-check all open browsers for results"""
        try:
            for driver in self.active_drivers:
                try:
                    driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);"
                    )
                    buttons = driver.find_elements(By.TAG_NAME, "button")
                    for button in buttons:
                        if button.is_displayed():
                            driver.execute_script("arguments[0].click();", button)
                    result = analyze_response(driver)
                    self.update_progress(driver.current_url, result)
                except:
                    continue
            self.results_text.insert(
                "end", "\n[FORCE] Results check completed! 💥\n", "force"
            )
            self.results_text.tag_config("force", foreground="#ff6b00")
            self.results_text.see("end")
        except Exception as e:
            self.results_text.insert(
                "end", "\n[FORCE] No active browsers to check! 🔍\n", "force"
            )
        def analyze_response(driver):
            """Nuclear-level response analysis"""
        success_patterns = [
            "//*[contains(text(), 'success')]",
            "//*[contains(text(), 'thank you')]",
            "//*[contains(text(), 'verify')]",
            "//*[contains(text(), 'confirmed')]",
            "//*[contains(text(), 'available')]",
            "//input[@type='submit']",
            "//button[@type='submit']",
        ]
        error_patterns = [
            "//*[contains(text(), 'error')]",
            "//*[contains(text(), 'invalid')]",
            "//*[contains(text(), 'taken')]",
            "//*[contains(text(), 'exists')]",
            "//*[contains(@class, 'error')]",
            "//*[contains(@class, 'invalid')]",
        ]
        for pattern in success_patterns:
            elements = driver.find_elements(By.XPATH, pattern)
            if elements and elements[0].is_displayed():
                return "Success: Email validation passed! ✅"
        for pattern in error_patterns:
            elements = driver.find_elements(By.XPATH, pattern)
            if elements and elements[0].is_displayed():
                return f"Error: {elements[0].text} ❌"
        return "Status: No clear validation result detected 🤔"
    def start_auto_kill(self):
        def auto_kill():
            while self.auto_kill_enabled:
                self.kill_stuck_browsers()
                time.sleep(7)
        self.auto_kill_thread = threading.Thread(target=auto_kill, daemon=True)
        self.auto_kill_thread.start()
    def toggle_auto_kill(self):
        self.auto_kill_enabled = not self.auto_kill_enabled
        if self.auto_kill_enabled:
            self.kill_button.configure(text="AUTO-KILL ENABLED", fg_color="#ff0000")
            self.start_auto_kill()
        else:
            self.kill_button.configure(text="AUTO-KILL DISABLED", fg_color="#666666")
    def kill_stuck_browsers(self):
        try:
            if platform.system() == "Windows":
                os.system("taskkill /F /IM chrome.exe")
                os.system("taskkill /F /IM chromedriver.exe")
            else:
                os.system("pkill -f chrome")
                os.system("pkill -f chromedriver")
            self.results_text.insert(
                "end", "[KILL] Terminated all stuck browsers!\n", "error"
            )
            self.results_text.see("end")
        except:
            self.results_text.insert(
                "end", "[KILL] Failed to terminate browsers!\n", "error"
            )
            self.results_text.see("end")
    def create_main_frame(self):
        main_frame = ctk.CTkFrame(self, fg_color=THEME["bg_light"])
        main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.results_text = ctk.CTkTextbox(
            main_frame,
            fg_color=THEME["bg_dark"],
            text_color=THEME["text"],
            font=("Roboto Mono", 12),
            border_color=THEME["accent"],
            border_width=2,
        )
        self.results_text.pack(fill="both", expand=True, padx=20, pady=20)
    def create_status_frame(self):
        status_frame = ctk.CTkFrame(self, fg_color=THEME["bg_light"], height=100)
        status_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(10, 20))
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ctk.CTkProgressBar(
            status_frame,
            variable=self.progress_var,
            progress_color=THEME["accent"],
            height=20,
            border_color=THEME["accent"],
        )
        self.progress_bar.pack(fill="x", padx=20, pady=(20, 5))
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="Ready to start validation",
            font=("Roboto", 14, "bold"),
            text_color=THEME["text"],
        )
        self.status_label.pack(pady=5)
        def validation_thread():
            total_platforms = len(PLATFORM)
            for platform in PLATFORM:
                if not self.running:
                    break
                try:
                    platform_name, email, result = test_email_enhanced(email, platform)
                    self.completed_tests += 1
                    progress = self.completed_tests / total_platforms
                    self.after(10, lambda: self.progress_var.set(progress))
                    self.after(10, lambda: self.update_progress(platform_name, result))
                except Exception as e:
                    self.after(
                        10,
                        lambda: self.update_progress(
                            platform["name"], f"Error: {str(e)}"
                        ),
                    )
            self.after(
                10, lambda: self.status_label.configure(text="Validation completed")
            )
            self.after(10, lambda: self.start_button.configure(state="normal"))
            self.after(10, lambda: self.stop_button.configure(state="disabled"))
            self.running = False
        threading.Thread(target=validation_thread, daemon=True).start()
    def start_validation(self):
        input_email = self.email_entry.get().strip()
        if not input_email or "@" not in input_email:
            messagebox.showerror("Error", "Please enter a valid email address")
            return
        self.running = True
        self.completed_tests = 0
        self.progress_var.set(0)
        self.results_text.delete("1.0", "end")
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.status_label.configure(text="RAPID VALIDATION IN PROGRESS! 🚀")
        def validation_thread():
            with ThreadPoolExecutor(
                max_workers=10
            ) as executor:  # Run 10 tests simultaneously!
                futures = []
                for platform in PLATFORM:
                    if not self.running:
                        break
                    futures.append(
                        executor.submit(test_email_enhanced, input_email, platform)
                    )
                for future in futures:
                    if not self.running:
                        break
                    try:
                        platform_name, result = future.result()
                        self.completed_tests += 1
                        progress = self.completed_tests / self.total_tests
                        self.after(10, lambda p=progress: self.progress_var.set(p))
                        self.after(
                            10,
                            lambda n=platform_name, r=result: self.update_progress(
                                n, r
                            ),
                        )
                        self.after(
                            10,
                            lambda: self.status_label.configure(
                                text=f"RAPID TESTING: {self.completed_tests}/{self.total_tests} 🔥"
                            ),
                        )
                    except Exception as e:
                        continue
        threading.Thread(target=validation_thread, daemon=True).start()
    def validate_email_input(self, email):
        if not email or "@" not in email:
            self.show_error("Invalid Email", "Please enter a valid email address")
            return False
        if not validate_email_format(email):
            self.show_error("Format Error", "Invalid email format")
            return False
        if not check_mx_records(email):
            self.show_error("Domain Error", "Invalid domain MX records")
            return False
        if is_disposable_email(email):
            self.show_error("Security Error", "Disposable email detected")
            return False
        return True
    def run_validation(self, email):
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for platform in PLATFORM:
                if not self.running:
                    break
                futures.append(executor.submit(test_email_enhanced, email, platform))
            for future in futures:
                if not self.running:
                    break
                platform_name, email, result = future.result()
                self.process_result(platform_name, result)
        self.show_final_summary()
    def process_result(self, platform_name, result):
        self.update_progress(platform_name, result)
        if "Success" in result:
            self.working_sites.append(platform_name)
            self.total_successes += 1
    def show_final_summary(self):
        if self.running:
            success_rate = (self.total_successes / self.total_tests) * 100
            summary_text = f"\n=== VALIDATION SUMMARY ===\n"
            summary_text += f"Total Sites Tested: {self.total_tests}\n"
            summary_text += f"Working Sites: {len(self.working_sites)}\n"
            summary_text += f"Success Rate: {success_rate:.1f}%\n"
            if len(self.working_sites) >= 3:
                summary_text += "\n✅ EMAIL VALIDATED SUCCESSFULLY\n"
                summary_color = THEME["success"]
            else:
                summary_text += "\n❌ VALIDATION FAILED\n"
                summary_color = THEME["error"]
            self.results_text.insert("end", summary_text, "summary")
            self.results_text.tag_config("summary", foreground=summary_color)
        self.reset_ui_state()
    def show_error(self, title, message):
        messagebox.showerror(title, message)
    def reset_validation_state(self):
        self.running = True
        self.completed_tests = 0
        self.total_successes = 0
        self.working_sites = []
        self.progress_var.set(0)
        self.results_text.delete("1.0", "end")
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
    def reset_ui_state(self):
        self.status_label.configure(text="Validation completed")
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.running = False
    def stop_validation(self):
        self.running = False
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        self.status_label.configure(text="Validation stopped")
    def update_progress(self, platform_name, result):
        self.completed_tests += 1
        progress = self.completed_tests / self.total_tests
        self.progress_var.set(progress)  # Update progress bar
        timestamp = datetime.now().strftime("%H:%M:%S")
        result_color = THEME["success"] if "Success" in result else THEME["error"]
        self.results_text.insert("end", f"[{timestamp}] {platform_name}: ", "timestamp")
        self.results_text.insert("end", f"{result}\n", "result")
        self.results_text.tag_config("timestamp", foreground="#888888")
        self.results_text.tag_config("result", foreground=result_color)
        self.results_text.see("end")
        self.status_label.configure(
            text=f"🚀 Testing Progress: {self.completed_tests}/{self.total_tests} sites checked!"
        )
def validate_email_format(email):
    """Validate email format using regex and basic rules"""
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
def check_mx_records(email):
    """Check if email domain has valid MX records"""
    domain = email.split("@")[1]
    try:
        mx_records = dns.resolver.resolve(domain, "MX")
        return len(mx_records) > 0
    except:
        return False
def is_disposable_email(email):
    """Check if email is from a disposable domain"""
    domain = email.split("@")[1]
    try:
        response = requests.get(f"https://open.kickbox.com/v1/disposable/{domain}")
        return response.json().get("disposable", False)
    except:
        return False
def check_validation_messages(driver):
    """Check for validation messages on the page"""
    validation_patterns = [
        "//div[contains(@class, 'error')]",
        "//span[contains(@class, 'error')]",
        "//p[contains(@class, 'error')]",
        "//*[contains(text(), 'already exists')]",
        "//*[contains(text(), 'invalid')]",
    ]
    for pattern in validation_patterns:
        elements = driver.find_elements(By.XPATH, pattern)
        if elements:
            return f"Error: {elements[0].text}"
    return None
def submit_and_analyze(driver, platform):
    """Submit form and analyze response"""
    try:
        submit_buttons = driver.find_elements(
            By.XPATH,
            "//button[@type='submit'] | //input[@type='submit'] | //button[contains(text(), 'Sign Up')]",
        )
        if submit_buttons:
            simulate_human_behavior(driver, submit_buttons[0])
            submit_buttons[0].click()
            time.sleep(random.uniform(2, 4))
            for pattern in platform.get("success_patterns", []):
                elements = driver.find_elements(
                    By.XPATH, f"//*[contains(text(), '{pattern}')]"
                )
                if elements:
                    return True
            current_url = driver.current_url
            if "verify" in current_url or "confirm" in current_url:
                return True
    except Exception as e:
        logger.error(f"Submit analysis error: {str(e)}")
    return False
def enhance_driver_options(options):
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--disable-web-security")
    options.add_argument(
        "--disable-features=IsolateOrigins,site-per-process,TranslateUI"
    )
    options.add_argument("--disable-blink-features=AutomationControlled")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.managed_default_content_settings.images": 1,
        "profile.default_content_setting_values.cookies": 1,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation", "enable-logging", "ignore-certificate-errors"],
    )
    return options
def test_email_enhanced(email, platform):
    options = Options()
    options = enhance_driver_options(options)
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(platform["url"])
        wait = WebDriverWait(driver, 20)
        overlay_selectors = [
            "div[class*='overlay']",
            "div[class*='modal']",
            "div[class*='popup']",
            "div[class*='cookie']",
            "div[id*='overlay']",
            "div[id*='modal']",
            "iframe[id*='popup']",
            ".overlay",
            ".modal",
            ".popup",
            ".cookie-banner",
            "div[class*='dialog']",
            "div[class*='notification']",
            "div[class*='alert']",
            "div[class*='banner']",
            "div[class*='drawer']",
            "div[class*='toast']",
            "div[role='dialog']",
            "div[role='alertdialog']",
            "div[class*='MuiDialog']",
            "div[class*='ReactModal']",
            "div[class*='v-dialog']",
            "div[class*='ant-modal']",
            "//div[contains(@class, 'overlay')]",
            "//div[contains(@class, 'modal')]",
            "//div[@aria-modal='true']",
            "//div[contains(@style,'z-index')]",
        ]
        for selector in overlay_selectors:
            try:
                elements = driver.find_elements(
                    By.CSS_SELECTOR if not selector.startswith("//") else By.XPATH,
                    selector,
                )
                for element in elements:
                    driver.execute_script(
                        """
                        arguments[0].remove();
                        arguments[0].style.display = 'none';
                        arguments[0].style.visibility = 'hidden';
                        arguments[0].style.opacity = '0';
                    """,
                        element,
                    )
            except:
                continue
        driver.execute_script(
            """
            var elements = document.getElementsByTagName('*');
            for (var i = 0; i < elements.length; i++) {
                elements[i].style.zIndex = 'auto';
                elements[i].style.pointerEvents = 'auto';
                elements[i].style.overflow = 'visible';
                elements[i].style.position = 'relative';
            }
            document.body.style.overflow = 'visible';
            document.documentElement.style.overflow = 'visible';
        """
        )
        email_selectors = [
            f"#{platform['email_id']}",
            "input[type='email']",
            "input[type='text']",
            "input[name='email']",
            "input[name='email_address']",
            "input[name='emailAddress']",
            "input[name='user_email']",
            "input[name='userEmail']",
            "input[name='mail']",
            "input[name='e-mail']",
            "input[name='account_email']",
            "input[name='accountEmail']",
            "input[name='login_email']",
            "input[name='loginEmail']",
            "input[name='register_email']",
            "input[name='registerEmail']",
            "input[name='signup_email']",
            "input[name='signupEmail']",
            "input[data-testid='riot-signup-email']",
            "input[data-testid='epic-email']",
            "input[data-testid='steam-email']",
            "input[data-testid='origin-email']",
            "input[data-testid='battlenet-email']",
            "input[data-testid='uplay-email']",
            "input[data-testid='xbox-email']",
            "input[data-testid='psn-email']",
            "input[data-testid='nintendo-email']",
            "input[data-testid='game-email']",
            "input[data-testid='gaming-email']",
            "input[formcontrolname='email']",
            "input[formcontrolname='mail']",
            "input[ng-model='email']",
            "input[ng-model='mail']",
            "input[v-model='email']",
            "input[v-model='mail']",
            "input[data-bind='value: email']",
            "input[data-bind='textInput: email']",
            "input[[(ngModel)]='email']",
            "input[formControl='email']",
            "input[form-control='email']",
            "input[data-reactid*='email']",
            "input[data-react*='email']",
            "input[react-email]",
            "input[react-mail]",
            "input[data-react-email]",
            "input[data-react-mail]",
            "input[reactemail]",
            "input[reactmail]",
            "input[data-v-email]",
            "input[v-email]",
            "input[vue-email]",
            "input[vue-mail]",
            "input[data-vue-email]",
            "input[data-vue-mail]",
            "input[vueemail]",
            "input[vuemail]",
            "input[ng-reflect-name='email']",
            "input[ng-reflect-model='email']",
            "input[angular-email]",
            "input[angular-mail]",
            "input[data-angular-email]",
            "input[data-angular-mail]",
            "input[angularemail]",
            "input[angularmail]",
            "input[data-testid*='email']",
            "input[data-test*='email']",
            "input[data-qa*='email']",
            "input[data-cy*='email']",
            "input[data-automation*='email']",
            "input[data-auto*='email']",
            "input[data-e2e*='email']",
            "input[data-selenium*='email']",
            "input[data-test-automation*='email']",
            "input#email-input",
            "input#mail-input",
            "input#email-field",
            "input#mail-field",
            "input#email_field",
            "input#mail_field",
            "input#emailField",
            "input#mailField",
            "input#email-control",
            "input#mail-control",
            "input.email-input",
            "input.mail-input",
            "input.email-field",
            "input.mail-field",
            "input.email_field",
            "input.mail_field",
            "input.emailField",
            "input.mailField",
            "input.email-control",
            "input.mail-control",
            "input[id*='email']",
            "input[id*='mail']",
            "input[name*='email']",
            "input[name*='mail']",
            "input[class*='email']",
            "input[class*='mail']",
            "input[placeholder*='email']",
            "input[placeholder*='mail']",
            "input[title*='email']",
            "input[title*='mail']",
            "input[aria-label*='email']",
            "input[aria-label*='mail']",
            "input[aria-labelledby*='email']",
            "input[aria-labelledby*='mail']",
            "input[aria-describedby*='email']",
            "input[aria-describedby*='mail']",
            "input[aria-details*='email']",
            "input[aria-details*='mail']",
            "input[data-field='email']",
            "input[data-input='email']",
            "input[data-type='email']",
            "input[data-form='email']",
            "input[data-validation='email']",
            "input[data-target='email']",
            "input[data-bind='email']",
            "input[data-control='email']",
            "input[data-element='email']",
            "input[data-component='email']",
            "//input[contains(translate(@name,'EMAIL','email'),'email')]",
            "//input[contains(translate(@id,'EMAIL','email'),'email')]",
            "//input[contains(translate(@class,'EMAIL','email'),'email')]",
            "//input[contains(translate(@placeholder,'EMAIL','email'),'email')]",
            "//input[contains(translate(@aria-label,'EMAIL','email'),'email')]",
            "//div[contains(@class,'form')]//div[contains(@class,'field')]//input",
            "//div[contains(@class,'signup')]//div[contains(@class,'input')]//input",
            "//div[contains(@class,'register')]//div[contains(@class,'field')]//input",
            "//div[contains(@class,'login')]//div[contains(@class,'input')]//input",
            "//div[contains(@class,'email')]//input[not(@type='hidden')]",
            "//div[contains(@class,'mail')]//input[not(@type='hidden')]",
            "//form//div[contains(@class,'input')]//input[not(@type='hidden')]",
            "//label[contains(text(),'Email')]//following::input[1]",
            "//label[contains(text(),'Mail')]//following::input[1]",
            "//label[contains(text(),'E-mail')]//following::input[1]",
            "//label[contains(.,'Email')]//following::input[1]",
            "//label[contains(.,'Mail')]//following::input[1]",
            "//label[@for='email']//following::input[1]",
            "//span[contains(text(),'Email')]//following::input[1]",
            "//span[contains(text(),'Mail')]//following::input[1]",
            "//div[contains(text(),'Email')]//following::input[1]",
            "//div[contains(text(),'Mail')]//following::input[1]",
            "//form//div[contains(@class,'field')]//input[@type='text' or @type='email']",
            "//form//div[contains(@class,'input')]//input[@type='text' or @type='email']",
            "//form//div[contains(@class,'control')]//input[@type='text' or @type='email']",
            "//*[@id='shadow-root']//input[@type='email']",
            "//*[@id='shadow-root']//input[contains(@name,'email')]",
            "//*[@id='shadow-root']//input[contains(@id,'email')]",
            "//*[@id='shadow-root']//input[contains(@class,'email')]",
            "//iframe//input[@type='email']",
            "//iframe//input[contains(@name,'email')]",
            "//iframe//input[contains(@id,'email')]",
            "//iframe//input[contains(@class,'email')]",
            "input[name='contact_email']",
            "input[name='primary_email']",
            "input[name='secondary_email']",
            "input[name='recovery_email']",
            "input[name='alternate_email']",
            "input[name='business_email']",
            "input[name='personal_email']",
            "input[name='work_email']",
            "input[name='corporate_email']",
            "input.form-control.email",
            "input.input-field.email",
            "input.form-input.email",
            "input.field-input.email",
            "input.control-input.email",
            "input[type='email'][required]",
            "input[type='text'][required][name*='email']",
            "input[type='text'][name*='email'][class*='input']",
            "input[type='text'][class*='email'][required]",
            "input[pattern='[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$']",
            "input[pattern*='@'][type='text']",
            "input[pattern*='@'][type='email']",
            "input[type='text'][autocomplete='email']",
            "input[type='text'][spellcheck='false'][autocomplete='email']",
            "input[type='text'][autocapitalize='none'][autocomplete='email']",
            "input[type='text'][autocorrect='off'][name*='email']",
            "input[type='text'][data-lpignore='true'][name*='email']",
            "input[name*='game'][type='email']",
            "input[class*='game'][type='email']",
            "input[id*='game'][type='email']",
            "input[data-game*='email']",
            "input[data-gaming*='email']",
            "input[class*='registration'][type='email']",
            "input[data-steam*='email']",
            "input[data-epic*='email']",
            "input[data-riot*='email']",
            "input[data-blizzard*='email']",
            "input[data-origin*='email']",
            "input[data-ubisoft*='email']",
            "input[data-bethesda*='email']",
            "input[data-rockstar*='email']",
            "input[data-nintendo*='email']",
            "input[data-psn*='email']",
            "input[data-xbox*='email']",
            "//div[contains(@class,'signup') or contains(@class,'register')]//input[contains(@type,'email') or contains(@type,'text')]",
            "//div[contains(@class,'form') or contains(@class,'input')]//input[@type='email' or contains(@name,'email')]",
            "//form[contains(@class,'signup') or contains(@class,'register')]//input[not(@type='hidden')]",
            "//div[contains(@class,'email-wrapper') or contains(@class,'input-wrapper')]//input",
            "input[data-vv-name*='email']",
            "input[data-vee*='email']",
            "input[data-formik*='email']",
            "input[data-redux*='email']",
            "input[data-mobx*='email']",
            "input[data-vuex*='email']",
            "input[data-ngrx*='email']",
            "input.signup__email",
            "input.register__email",
            "input.auth__email",
            "input.login__email",
            "input.form__email",
            "input.input__email",
            "input.field__email",
            "input.control__email",
            "input[data-dynamic*='email']",
            "input[data-field*='email']",
            "input[data-input*='email']",
            "input[data-form*='email']",
            "input[data-dynamic-field*='email']",
            "//*[contains(@*,'email')]",
            "//*[contains(@*,'mail')]",
            "//input[matches(name,'.*[email|mail].*','i')]",
            "//input[matches(id,'.*[email|mail].*','i')]",
            "//input[matches(@*,'.*[email|mail].*','i')]",
            "//input[not(@type='hidden')][not(@type='checkbox')][not(@type='radio')][not(@type='submit')]",
            "//input[string-length(@name)>0][not(@type='hidden')]",
            "//*[self::input or self::textarea][not(@type='hidden')]",
            "//div[contains(@class,'control')]//input[not(@type='hidden')]",
            "//div[contains(@class,'field')]//input[not(@type='hidden')]",
            "//div[contains(@class,'input')]//input[not(@type='hidden')]",
            "//*[contains(translate(string(),'EMAILMAILADDRESSCONTACT','emailmailaddresscontact'),'email')]//input",
            "//*[contains(translate(string(),'EMAILMAILADDRESSCONTACT','emailmailaddresscontact'),'mail')]//input",
            "//*[contains(translate(@*,'EMAILMAILADDRESSCONTACT','emailmailaddresscontact'),'email')]",
            "//*[contains(translate(@*,'EMAILMAILADDRESSCONTACT','emailmailaddresscontact'),'mail')]"
            "//ancestor::*[contains(@class,'form')]//input[not(@type='hidden')]",
            "//ancestor::*[contains(@class,'signup')]//input[not(@type='hidden')]",
            "//ancestor::*[contains(@class,'register')]//input[not(@type='hidden')]",
            "input[data-svelte*='email']",
            "input[data-solid*='email']",
            "input[data-preact*='email']",
            "input[data-lit*='email']",
            "input[data-stencil*='email']",
            "input[data-polymer*='email']",
            "input[type='text'][inputmode='email']",
            "input[type='text'][autocomplete='username']",
            "input[type='text'][role='textbox'][name*='email']",
            "input[type='text'][enterkeyhint='next'][name*='email']",
            "//descendant::input[not(@type='hidden')]",
            "//descendant::*[contains(@class,'email')]//input",
            "//descendant::*[contains(@class,'mail')]//input",
            "input[data-gog*='email']",
            "input[data-ea*='email']",
            "input[data-valve*='email']",
            "input[data-activision*='email']",
            "input[data-square-enix*='email']",
            "input[data-bandai*='email']",
            "input[data-konami*='email']",
            "input[data-capcom*='email']",
            "input[data-sega*='email']",
            "//input[matches(@*,'^.*e.*m.*a.*i.*l.*$','i')]",
            "//input[matches(@*,'^.*m.*a.*i.*l.*$','i')]",
            "//input[matches(@*,'.*contact.*','i')]",
            "input.js-email-input",
            "input.js-mail-input",
            "input.js-contact-email",
            "input.js-user-email",
            "input.js-account-email",
            "//fieldset//input[not(@type='hidden')]",
            "//fieldset[contains(@class,'email')]//input",
            "//fieldset[contains(@class,'contact')]//input",
            "input[data-hook*='email']",
            "input[data-ref*='email']",
            "input[data-element*='email']",
            "input[data-component*='email']",
            "//input[@tabindex and not(@type='hidden')]",
            "//input[@autofocus and not(@type='hidden')]",
            "//input[contains(@class,'required') and not(@type='hidden')]",
            "//*[contains(@class,'input-container')]//input[not(@type='hidden')]",
            "//*[contains(@class,'field-container')]//input[not(@type='hidden')]",
            "//*[contains(@class,'form-container')]//input[not(@type='hidden')]",
            "//body//form//input[not(@type='hidden')]",
            "//*[contains(@role,'form')]//input[not(@type='hidden')]",
            "//*[@data-testid]//input[not(@type='hidden')]",
        ]
        entry_methods = [
            lambda el: el.send_keys(email),
            lambda el: driver.execute_script(f"arguments[0].value = '{email}';", el),
            lambda el: [el.send_keys(c) for c in email],
            lambda el: driver.execute_script(
                f"""
                arguments[0].focus();
                arguments[0].value = '{email}';
                arguments[0].dispatchEvent(new Event('input', {{ bubbles: true }}));
                arguments[0].dispatchEvent(new Event('change', {{ bubbles: true }}));
            """,
                el,
            ),
            lambda el: ActionChains(driver)
            .move_to_element(el)
            .click()
            .send_keys(email)
            .perform(),
            lambda el: driver.execute_script(
                f"""
                arguments[0].focus();
                arguments[0].select();
                arguments[0].value = '{email}';
                arguments[0].dispatchEvent(new InputEvent('input'));
                arguments[0].dispatchEvent(new Event('change'));
            """,
                el,
            ),
            lambda el: driver.execute_script(
                """
                function setEmailInShadowDOM(element, email) {
                    if (element.shadowRoot) {
                        let input = element.shadowRoot.querySelector('input[type="email"]');
                        if (input) input.value = email;
                    }
                    element.value = email;
                }
                setEmailInShadowDOM(arguments[0], arguments[1]);
            """,
                el,
                email,
            ),
        ]
        success = False
        for selector in email_selectors:
            try:
                email_input = wait.until(
                    EC.presence_of_element_located(
                        (
                            (
                                By.CSS_SELECTOR
                                if not selector.startswith("//")
                                else By.XPATH
                            ),
                            selector,
                        )
                    )
                )
                for method in entry_methods:
                    try:
                        method(email_input)
                        entered_value = driver.execute_script(
                            "return arguments[0].value;", email_input
                        )
                        if email in entered_value:
                            success = True
                            break
                    except:
                        continue
                if success:
                    break
            except:
                continue
        if not success:
            return (
                platform["name"],
                email,
                "Error: Could not enter email after all attempts",
            )
        return platform["name"], email, "Success: Email entered successfully"
    except Exception as e:
        return platform["name"], email, f"Error: {str(e)}"
    finally:
        driver.quit()
def inject_stealth_scripts(driver):
    js_scripts = [
        """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        """,
        """
        Object.defineProperty(navigator, 'plugins', {
            get: () => [
                {description: "PDF Viewer", filename: "internal-pdf-viewer"},
                {description: "Chrome PDF Viewer", filename: "chrome-pdf-viewer"},
                {description: "Native Client", filename: "native-client"}
            ]
        });
        """,
        """
        window.chrome = {
            runtime: {},
            loadTimes: function() {},
            csi: function() {},
            app: {}
        };
        """,
    ]
    for script in js_scripts:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {"source": script}
        )
def simulate_human_behavior(driver, element):
    actions = ActionChains(driver)
    for _ in range(random.randint(2, 4)):
        x_offset = random.randint(-100, 100)
        y_offset = random.randint(-100, 100)
        actions.move_by_offset(x_offset, y_offset)
        time.sleep(random.uniform(0.1, 0.3))
    actions.move_to_element(element)
    actions.pause(random.uniform(0.5, 1.0))
    driver.execute_script(f"window.scrollBy(0, {random.randint(-200, 200)})")
    time.sleep(random.uniform(0.3, 0.7))
    actions.perform()
def simulate_page_interaction(driver):
    scroll_amounts = [300, -150, 200, -100]
    for amount in random.sample(scroll_amounts, 2):
        driver.execute_script(f"window.scrollBy(0, {amount})")
        time.sleep(random.uniform(0.5, 1.5))
    actions = ActionChains(driver)
    for _ in range(random.randint(2, 4)):
        actions.move_by_offset(
            random.randint(-100, 100), random.randint(-100, 100)
        ).perform()
        time.sleep(random.uniform(0.2, 0.6))
def type_humanlike(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))
        if random.random() < 0.05:
            element.send_keys(Keys.BACKSPACE)
            time.sleep(random.uniform(0.1, 0.3))
            element.send_keys(char)
            time.sleep(random.uniform(0.2, 0.4))
def handle_platform_specific(driver, platform_name):
    platform_handlers = {
        "Epic Games": handle_epic,
        "Steam": handle_steam,
        "Riot Games": handle_riot,
        "Battle.net": handle_battlenet,
    }
    if platform_name in platform_handlers:
        platform_handlers[platform_name](driver)
def handle_steam(driver):
    try:
        age_check = "//select[@name='year']"
        if element_exists(driver, age_check):
            Select(driver.find_element(By.XPATH, age_check)).select_by_value("1990")
            driver.find_element(
                By.XPATH, "//span[contains(text(),'View Page')]"
            ).click()
        captcha_frame = "//iframe[contains(@src,'captcha')]"
        if element_exists(driver, captcha_frame):
            pass
    except Exception as e:
        log_platform_error("Steam", str(e))
def handle_riot(driver):
    try:
        birthday_fields = {
            "day": "//input[@name='date_of_birth_day']",
            "month": "//input[@name='date_of_birth_month']",
            "year": "//input[@name='date_of_birth_year']",
        }
        for field, xpath in birthday_fields.items():
            if element_exists(driver, xpath):
                element = driver.find_element(By.XPATH, xpath)
                if field == "day":
                    element.send_keys("01")
                elif field == "month":
                    element.send_keys("01")
                elif field == "year":
                    element.send_keys("1990")
        region_selector = "//select[@name='region']"
        if element_exists(driver, region_selector):
            Select(driver.find_element(By.XPATH, region_selector)).select_by_value("NA")
    except Exception as e:
        log_platform_error("Riot", str(e))
def handle_battlenet(driver):
    try:
        country_selector = "//select[@name='country']"
        if element_exists(driver, country_selector):
            Select(driver.find_element(By.XPATH, country_selector)).select_by_value(
                "US"
            )
        sms_skip = "//a[contains(text(),'Skip')]"
        if element_exists(driver, sms_skip):
            driver.find_element(By.XPATH, sms_skip).click()
    except Exception as e:
        log_platform_error("Battle.net", str(e))
def element_exists(driver, xpath, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return True
    except:
        return False
def log_platform_error(platform, error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_log = f"[{timestamp}] {platform} Error: {error}\n"
    with open("platform_errors.log", "a") as f:
        f.write(error_log)
class AdvancedValidationPatterns:
    def __init__(self):
        self.patterns = {
            "success": [
                r"verification.*sent",
                r"check.*email",
                r"confirm.*email",
                r"verify.*account",
                r"welcome.*aboard",
                r"registration.*success",
                r"account.*created",
                r"thank.*you.*registering",
            ],
            "error": [
                r"email.*already.*exists",
                r"account.*already.*exists",
                r"invalid.*email",
                r"email.*not.*valid",
                r"please.*try.*again",
                r"error.*occurred",
                r"registration.*failed",
            ],
        }
def handle_epic(driver):
    try:
        captcha_bypass = "//div[contains(@class, 'captcha')]"
        age_verify = "//div[contains(@class, 'age-gate')]//button"
        tos_accept = (
            "//div[contains(@class, 'tos')]//button[contains(text(), 'Accept')]"
        )
        elements_to_handle = [captcha_bypass, age_verify, tos_accept]
        for element in elements_to_handle:
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, element))
                ).click()
            except:
                continue
    except:
        pass
def handle_popups(driver):
    popup_patterns = [
        "//button[contains(., 'Accept')]",
        "//button[contains(., 'Accept All')]",
        "//button[contains(., 'Allow')]",
        "//button[contains(., 'Allow All')]",
        "//button[contains(., 'Agree')]",
        "//button[contains(., 'I Agree')]",
        "//button[contains(., 'Continue')]",
        "//button[contains(., 'Proceed')]",
        "//button[contains(., 'Got it')]",
        "//button[contains(., 'Okay')]",
        "//button[contains(., 'OK')]",
        "//button[contains(., 'Skip')]",
        "//button[contains(., 'Close')]",
        "//button[contains(., 'Dismiss')]",
        "//button[contains(., 'Not Now')]",
        "//button[contains(., 'Maybe Later')]",
        "//button[contains(., 'No Thanks')]",
        "//button[contains(., 'Later')]",
        "//button[contains(., 'Next Time')]",
        "//button[contains(., 'Cookie')]",
        "//button[contains(., 'Accept Cookies')]",
        "//button[contains(., 'Allow Cookies')]",
        "//button[contains(., 'Accept All Cookies')]",
        "//button[contains(., 'Allow Essential Cookies')]",
        "//button[contains(., 'Accept Selected')]",
        "//button[contains(., 'Accept Choice')]",
        "//button[contains(., 'Save Preferences')]",
        "//button[contains(., 'Save Settings')]",
        "//button[contains(., 'Confirm Choices')]",
        "//button[contains(., 'Privacy')]",
        "//button[contains(., 'Accept Privacy')]",
        "//button[contains(., 'Privacy Policy')]",
        "//button[contains(., 'Accept Policy')]",
        "//button[contains(., 'Accept Terms')]",
        "//button[contains(., 'Accept All Terms')]",
        "//button[contains(., 'Enable')]",
        "//button[contains(., 'Turn On')]",
        "//button[contains(., 'Subscribe')]",
        "//button[contains(., 'Allow Notifications')]",
        "//button[contains(., 'Enable Notifications')]",
        "//button[contains(., 'Yes')]",
        "//button[contains(., 'No')]",
        "//button[contains(., 'Stay')]",
        "//button[contains(., 'Continue to')]",
        "//button[contains(., 'Remain')]",
        "//button[contains(., 'This Site')]",
        "//button[contains(., 'This Version')]",
        "//div[contains(@class, 'popup')]//button",
        "//div[contains(@class, 'modal')]//button",
        "//div[contains(@class, 'dialog')]//button",
        "//div[contains(@class, 'overlay')]//button",
        "//div[contains(@class, 'cookie')]//button",
        "//div[contains(@class, 'consent')]//button",
        "//div[contains(@class, 'notice')]//button",
        "//div[contains(@class, 'notification')]//button",
        "//div[contains(@class, 'alert')]//button",
        "//div[contains(@class, 'banner')]//button",
        "//div[contains(@class, 'drawer')]//button",
        "//div[contains(@class, 'toast')]//button",
        "//div[contains(@class, 'snackbar')]//button",
        "//div[contains(@class, 'prompt')]//button",
        "//div[contains(@class, 'lightbox')]//button",
        "//div[contains(@id, 'popup')]//button",
        "//div[contains(@id, 'modal')]//button",
        "//div[contains(@id, 'dialog')]//button",
        "//div[contains(@id, 'overlay')]//button",
        "//div[contains(@id, 'cookie')]//button",
        "//div[contains(@id, 'consent')]//button",
        "//div[contains(@id, 'notice')]//button",
        "//div[contains(@id, 'notification')]//button",
        "//div[contains(@id, 'alert')]//button",
        "//div[contains(@id, 'banner')]//button",
        "//div[@role='dialog']//button",
        "//div[@role='alertdialog']//button",
        "//div[@role='alert']//button",
        "//div[@role='banner']//button",
        "//div[@role='complementary']//button",
        "//div[@aria-modal='true']//button",
        "//div[@aria-hidden='false']//button",
        "//div[contains(@aria-label, 'cookie')]//button",
        "//div[contains(@aria-label, 'consent')]//button",
        "//div[contains(@aria-label, 'privacy')]//button",
        "//div[contains(@data-testid, 'popup')]//button",
        "//div[contains(@data-testid, 'modal')]//button",
        "//div[contains(@data-testid, 'dialog')]//button",
        "//div[contains(@data-testid, 'cookie')]//button",
        "//div[contains(@data-testid, 'consent')]//button",
        "//div[contains(@class, 'modal-content')]//button",
        "//div[contains(@class, 'popup-content')]//button",
        "//div[contains(@class, 'dialog-content')]//button",
        "//div[contains(@class, 'cookie-content')]//button",
        "//div[contains(@class, 'consent-content')]//button",
        "//div[contains(@class, 'ReactModal')]//button",
        "//div[contains(@class, 'v-dialog')]//button",
        "//div[contains(@class, 'MuiDialog')]//button",
        "//div[contains(@class, 'ant-modal')]//button",
        "//div[contains(@class, 'el-dialog')]//button",
        "//button[@aria-label='Close']",
        "//button[@aria-label='Dismiss']",
        "//button[contains(@class, 'close')]",
        "//button[contains(@class, 'dismiss')]",
        "//button[contains(@class, 'cancel')]",
        "*[aria-label='Close']",
        "*[aria-label='Dismiss']",
        "//i[contains(@class, 'close')]/..",
        "//i[contains(@class, 'times')]/..",
        "//i[contains(@class, 'cross')]/..",
        "//span[contains(@class, 'close')]/..",
        "//span[contains(@class, 'times')]/..",
        "//button[contains(., 'Understood')]",
        "//button[contains(., 'I understand')]",
        "//button[contains(., 'Got It')]",
        "//button[contains(., 'Roger that')]",
        "//button[contains(., 'Sounds good')]",
        "//button[contains(., 'Akzeptieren')]",  # German
        "//button[contains(., 'Alle akzeptieren')]",
        "//button[contains(., 'Accepter')]",  # French
        "//button[contains(., 'Tout accepter')]",
        "//button[contains(., 'Aceptar')]",  # Spanish
        "//button[contains(., 'Aceptar todo')]",
        "//button[contains(., 'Accetta')]",  # Italian
        "//button[contains(., 'Accetta tutto')]",
        "//button[contains(., 'Aceitar')]",  # Portuguese
        "//button[contains(., 'Aceitar tudo')]",
        "//div[contains(@class, 'bootstrap-modal')]//button",
        "//div[contains(@class, 'modal-header')]//button",
        "//div[contains(@class, 'modal-footer')]//button",
        "//div[contains(@class, 'MuiDialog-root')]//button",
        "//div[contains(@class, 'MuiModal-root')]//button",
        "//div[contains(@class, 'chakra-modal')]//button",
        "//div[contains(@class, 'tailwind-modal')]//button",
        "//div[contains(@class, 'tw-modal')]//button",
        "//*[@id='shadow-root']//div[contains(@class, 'popup')]//button",
        "//*[@id='shadow-root']//div[contains(@class, 'modal')]//button",
        "//*[@id='shadow-root']//div[contains(@class, 'dialog')]//button",
        "//iframe//div[contains(@class, 'popup')]//button",
        "//iframe//div[contains(@class, 'modal')]//button",
        "//iframe//div[contains(@class, 'dialog')]//button",
        "//div[contains(@class, 'newsletter')]//button",
        "//div[contains(@class, 'subscribe')]//button",
        "//div[contains(@id, 'newsletter')]//button",
        "//div[contains(@id, 'subscribe')]//button",
        "//button[contains(., 'No, thanks')]",
        "//button[contains(., 'Not interested')]",
        "//button[contains(., 'I am over')]",
        "//button[contains(., 'Confirm Age')]",
        "//button[contains(., 'Enter Site')]",
        "//button[contains(., 'Yes, I am')]",
        "//div[contains(@class, 'gdpr')]//button",
        "//div[contains(@class, 'ccpa')]//button",
        "//div[contains(@class, 'consent-manager')]//button",
        "//div[contains(@class, 'privacy-manager')]//button",
        "//button[contains(., 'Manage Settings')]",
        "//button[contains(., 'Preferences')]",
        "//div[contains(@class, 'social')]//button[contains(@class, 'close')]",
        "//div[contains(@class, 'share')]//button[contains(@class, 'close')]",
        "//div[contains(@class, 'follow')]//button[contains(@class, 'close')]",
        "//div[contains(@class, 'survey')]//button",
        "//div[contains(@class, 'feedback')]//button",
        "//div[contains(@class, 'questionnaire')]//button",
        "//div[contains(@class, 'exit')]//button",
        "//div[contains(@class, 'leave')]//button",
        "//div[contains(@class, 'abandon')]//button",
        "//div[contains(@class, 'chat')]//button",
        "//div[contains(@class, 'messenger')]//button",
        "//div[contains(@class, 'intercom')]//button",
        "//div[contains(@class, 'drift')]//button",
        "//div[contains(@class, 'zendesk')]//button",
        "//div[contains(@class, 'promo')]//button",
        "//div[contains(@class, 'discount')]//button",
        "//div[contains(@class, 'offer')]//button",
        "//div[contains(@class, 'sale')]//button",
        "//div[contains(@class, 'login')]//button[contains(@class, 'close')]",
        "//div[contains(@class, 'register')]//button[contains(@class, 'close')]",
        "//div[contains(@class, 'signup')]//button[contains(@class, 'close')]",
        "//div[contains(@class, 'download')]//button",
        "//div[contains(@class, 'install')]//button",
        "//div[contains(@class, 'video-popup')]//button",
        "//div[contains(@class, 'player-modal')]//button",
        "//div[contains(@class, 'ad-modal')]//button",
        "//div[contains(@class, 'advertisement')]//button",
        "//div[contains(@class, 'sponsored')]//button",
        "//div[contains(@class, 'mobile-modal')]//button",
        "//div[contains(@class, 'mobile-popup')]//button",
        "//div[contains(@class, 'app-banner')]//button",
        "//div[contains(@class, 'pwa-prompt')]//button",
        "//div[contains(@class, 'install-app')]//button",
        "//div[contains(@class, 'game-popup')]//button",
        "//div[contains(@class, 'achievement')]//button",
        "//div[contains(@class, 'level-up')]//button",
        "//div[contains(@class, 'reward')]//button",
        "//div[contains(@class, 'loot-box')]//button",
        "*[@aria-modal='true']//button",
        "*[@role='dialog']//button",
        "*[contains(@class, 'modal-backdrop')]",
        "*[contains(@class, 'overlay-backdrop')]",
        "*[contains(@class, 'dialog-backdrop')]",
        "//div[contains(@class, 'dynamic-content')]//button",
        "//div[contains(@class, 'lazy-modal')]//button",
        "//div[contains(@class, 'async-popup')]//button",
        "//div[contains(@class, 'loading-content')]//button",
        "//div[contains(@class, 'ngx-modal')]//button",
        "//div[contains(@class, 'ng-modal')]//button",
        "//div[contains(@class, 'react-modal')]//button",
        "//div[contains(@class, 'vue-modal')]//button",
        "//div[contains(@class, 'svelte-modal')]//button",
        "//div[contains(@class, 'paywall')]//button",
        "//div[contains(@class, 'subscription')]//button",
        "//div[contains(@class, 'premium')]//button",
        "//div[contains(@class, 'member')]//button",
        "//div[contains(@class, 'notification-prompt')]//button",
        "//div[contains(@class, 'push-notification')]//button",
        "//div[contains(@class, 'browser-notification')]//button",
        "//div[contains(@class, 'region-select')]//button",
        "//div[contains(@class, 'language-select')]//button",
        "//div[contains(@class, 'country-select')]//button",
        "//div[contains(@class, 'timed-popup')]//button",
        "//div[contains(@class, 'delayed-modal')]//button",
        "//div[contains(@class, 'scheduled-popup')]//button",
        "//div[contains(@class, 'scroll-popup')]//button",
        "//div[contains(@class, 'scroll-modal')]//button",
        "//div[contains(@class, 'scroll-triggered')]//button",
        "//div[contains(@class, 'welcome')]//button",
        "//div[contains(@class, 'greeting')]//button",
        "//div[contains(@class, 'intro')]//button",
        "//div[contains(@class, 'error-modal')]//button",
        "//div[contains(@class, 'warning-popup')]//button",
        "//div[contains(@class, 'alert-dialog')]//button",
        "//div[contains(@class, 'interstitial')]//button",
        "//div[contains(@class, 'takeover')]//button",
        "//div[contains(@class, 'overlay-content')]//button",
        "//*[contains(@style,'z-index')]//button",
        "//*[contains(@style,'position: fixed')]//button",
        "//*[contains(@style,'position:fixed')]//button",
    ]
    for pattern in popup_patterns:
        try:
            elements = driver.find_elements(By.XPATH, pattern)
            for element in elements:
                if element.is_displayed():
                    element.click()
                    time.sleep(0.5)
        except:
            continue
class ProxyRotator:
    def __init__(self):
        self.proxies = self.load_proxies()
        self.current_index = 0
    def load_proxies(self):
        return [
            "socks5://proxy1.com:1080",
            "socks5://proxy2.com:1080",
            "http://proxy3.com:8080",
        ]
    def get_next_proxy(self):
        proxy = self.proxies[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.proxies)
        return proxy
class BrowserFingerprint:
    def __init__(self):
        self.screen_resolutions = [
            (1920, 1080),
            (1366, 768),
            (1440, 900),
            (1536, 864),
        ]
    def generate_fingerprint(self):
        return {
            "userAgent": UserAgent().random,
            "screenResolution": random.choice(self.screen_resolutions),
            "timezone": random.choice(["UTC-8", "UTC-7", "UTC-5", "UTC-4"]),
            "platform": random.choice(["Win32", "MacIntel", "Linux x86_64"]),
            "webglVendor": random.choice(
                ["Google Inc. (NVIDIA)", "Google Inc. (Intel)", "Google Inc. (AMD)"]
            ),
        }
class AutomationBypass:
    @staticmethod
    def inject_stealth_scripts(driver):
        scripts = [
            """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            """,
            """
            window.chrome = {
                runtime: {}
            };
            """,
            """
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                Promise.resolve({ state: Notification.permission }) :
                originalQuery(parameters)
            );
            """,
        ]
        for script in scripts:
            driver.execute_script(script)
class ValidationEnhancer:
    @staticmethod
    def analyze_response(driver, platform):
        validation_methods = [
            ValidationEnhancer._check_url_change,
            ValidationEnhancer._check_success_elements,
            ValidationEnhancer._check_error_elements,
            ValidationEnhancer._check_network_requests,
        ]
        for method in validation_methods:
            result = method(driver, platform)
            if result:
                return result
        return "Status: Validation incomplete"
    @staticmethod
    def _check_url_change(driver, platform):
        current_url = driver.current_url
        if "success" in current_url or "verify" in current_url:
            return "Success: Redirected to verification page"
        return None
class CaptchaHandler:
    def __init__(self):
        self.captcha_services = {
            "2captcha": "YOUR_2CAPTCHA_KEY",
            "anticaptcha": "YOUR_ANTICAPTCHA_KEY",
            "capsolver": "YOUR_CAPSOLVER_KEY",
        }
    def solve_captcha(self, driver, platform_name):
        captcha_types = {
            "recaptcha": self._handle_recaptcha,
            "hcaptcha": self._handle_hcaptcha,
            "funcaptcha": self._handle_funcaptcha,
            "imagecaptcha": self._handle_image_captcha,
        }
        for captcha_type, handler in captcha_types.items():
            if self._detect_captcha(driver, captcha_type):
                return handler(driver)
    def _detect_captcha(self, driver, captcha_type):
        captcha_patterns = {
            "recaptcha": "//iframe[contains(@src,'recaptcha')]",
            "hcaptcha": "//iframe[contains(@src,'hcaptcha')]",
            "funcaptcha": "//iframe[contains(@src,'funcaptcha')]",
            "imageaptcha": "//img[contains(@class,'captcha')]",
        }
        try:
            return driver.find_element(
                By.XPATH, captcha_patterns[captcha_type]
            ).is_displayed()
        except:
            return False
class NetworkInterceptor:
    def __init__(self, driver):
        self.driver = driver
        self.requests = []
    def start_monitoring(self):
        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd(
            "Network.setRequestInterception", {"patterns": [{"urlPattern": "*"}]}
        )
    def intercept_request(self, request):
        headers = request.get("headers", {})
        headers["User-Agent"] = UserAgent().random
        headers["Accept-Language"] = "en-US,en;q=0.9"
        headers["Accept"] = (
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        )
        return {"headers": headers}
class PlatformAutomator:
    def __init__(self, platform):
        self.platform = platform
        self.automation_patterns = {
            "Epic Games": self._automate_epic,
            "Steam": self._automate_steam,
            "Riot Games": self._automate_riot,
            "Battle.net": self._automate_battlenet,
        }
    def automate(self, driver):
        if self.platform["name"] in self.automation_patterns:
            return self.automation_patterns[self.platform["name"]](driver)
    def _automate_epic(self, driver):
        steps = [
            {"type": "input", "locator": "name", "value": "//input[@name='name']"},
            {
                "type": "input",
                "locator": "lastName",
                "value": "//input[@name='lastName']",
            },
            {
                "type": "input",
                "locator": "displayName",
                "value": "//input[@name='displayName']",
            },
            {
                "type": "checkbox",
                "locator": "terms",
                "value": "//input[@type='checkbox']",
            },
        ]
        self._execute_steps(driver, steps)
class ValidationLogger:
    def __init__(self):
        self.log_file = f"validation_log_{int(time.time())}.txt"
    def log_attempt(self, platform, email, result, details=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"[{timestamp}] Platform: {platform} | Email: {email} | Result: {result}"
        )
        if details:
            log_entry += f" | Details: {details}"
        with open(self.log_file, "a") as f:
            f.write(log_entry + "\n")
if __name__ == "__main__":
    app = ModernEmailTester()
    app.mainloop()

# End of cleanup by TheZ