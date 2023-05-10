import os
import glob
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_renderer
import selenium.webdriver as webdriver

# Set the path to your HTML files
path_to_html_files = os.path.join("..","notebooks","plots")

# Set the path to where you want to save the screenshots
path_to_screenshots = os.path.join("..","notebooks","plots","plots_png")

# Set the dimensions of the screenshots
width = 1200
height = 800

# Find all the HTML files in the directory
html_files = glob.glob(os.path.join(path_to_html_files, '*.html'))

# Create a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

# Define the window.waitFor() function
wait_script = """
window.waitFor = function(conditionFunction) {
    const poll = resolve => {
        if(conditionFunction()) resolve();
        else setTimeout(() => poll(resolve), 400);
    }
    return new Promise(poll);
}
"""

# Loop through the HTML files and take a screenshot of each one
for html_file in html_files:
    # Load the HTML file in the browser
    browser.get('file://' + os.path.abspath(html_file))
    # Define the window.waitFor() function on the page
    browser.execute_script(wait_script)
    # Wait for the page to render
    browser.execute_script('window.waitFor(() => !!window.dash)')
    # Take a screenshot of the page
    browser.set_window_size(width, height)
    screenshot_path = os.path.join(path_to_screenshots, os.path.splitext(os.path.basename(html_file))[0] + '.png')
    browser.save_screenshot(screenshot_path)

# Close the browser
browser.quit()