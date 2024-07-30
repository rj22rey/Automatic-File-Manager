<?php
/* 
Template Name: AI File Manager
*/
get_header();
?>

<div class="container">
    <div class="content">
        <h1>AI File Manager</h1>
        <p>Welcome to AI File Manager! Our service helps you organize your files efficiently using an intelligent file sorting script.</p>
        <p>Follow these simple steps to use the AI File Manager:</p>
        <ol>
            <li><strong>Download and Install Python:</strong>
                <ul>
                    <li><a href="https://www.python.org/downloads/" target="_blank">Download Python</a> from the official website.</li>
                    <li>Follow the installation instructions for your operating system.</li>
                    <li>Ensure that you add Python to your system's PATH during the installation process.</li>
                </ul>
            </li>
            <li><strong>Download the Script:</strong> Click the button below to download the AI File Manager script to your computer.</li>
            <li><strong>Locate the Script:</strong> Find the downloaded script (FileManager.py) in your Downloads folder or the location where you saved it.</li>
            <li><strong>Open a Terminal or Command Prompt:</strong> 
                <ul>
                    <li><strong>Windows:</strong> Press <code>Win + R</code>, type <code>cmd</code>, and press Enter.</li>
                    <li><strong>Mac:</strong> Open Finder, go to Applications, then Utilities, and double-click Terminal.</li>
                    <li><strong>Linux:</strong> Open your preferred terminal application.</li>
                </ul>
            </li>
            <li><strong>Navigate to the Script Location:</strong> Use the <code>cd</code> command to change the directory to where you downloaded the script. For example:
                <pre><code>cd Downloads</code></pre>
            </li>
            <li><strong>Run the Script:</strong> Type the following command and press Enter:
                <pre><code>python FileManager.py</code></pre>
                <p>If you have Python 3 installed, you might need to use:
                <pre><code>python3 FileManager.py</code></pre></p>
            </li>
            <li><strong>Follow the Prompts:</strong> The script will guide you through the rest of the process.</li>
        </ol>
        <a class="download-button" href="<?php echo get_template_directory_uri(); ?>/FileManager.py" download>Download AI File Manager Script</a>
    </div>
</div>

<footer>
    &copy; <?php echo date("Y"); ?> AI File Manager. All rights reserved.
</footer>

<?php get_footer(); ?>
