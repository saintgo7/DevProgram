<?php
/**
 * Plugin Name: My Custom Plugin
 * Plugin URI: https://example.com/my-custom-plugin
 * Description: A basic WordPress plugin demonstrating plugin development
 * Version: 1.0.0
 * Author: Your Name
 * Author URI: https://example.com
 * License: GPL2
 */

// Prevent direct access
if (!defined('ABSPATH')) {
    exit;
}

class MyCustomPlugin {
    private static $instance = null;

    public static function get_instance() {
        if (self::$instance === null) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        $this->init_hooks();
    }

    private function init_hooks() {
        add_action('admin_menu', [$this, 'add_admin_menu']);
        add_action('admin_init', [$this, 'register_settings']);
        add_shortcode('my_shortcode', [$this, 'shortcode_handler']);
    }

    public function add_admin_menu() {
        add_menu_page(
            'My Plugin',
            'My Plugin',
            'manage_options',
            'my-custom-plugin',
            [$this, 'admin_page'],
            'dashicons-admin-generic',
            20
        );
    }

    public function register_settings() {
        register_setting('my_plugin_settings', 'my_plugin_option');
    }

    public function admin_page() {
        ?>
        <div class="wrap">
            <h1>My Custom Plugin Settings</h1>
            <form method="post" action="options.php">
                <?php
                settings_fields('my_plugin_settings');
                do_settings_sections('my_plugin_settings');
                ?>
                <table class="form-table">
                    <tr>
                        <th scope="row">Plugin Option</th>
                        <td>
                            <input type="text" name="my_plugin_option"
                                   value="<?php echo esc_attr(get_option('my_plugin_option')); ?>" />
                        </td>
                    </tr>
                </table>
                <?php submit_button(); ?>
            </form>
        </div>
        <?php
    }

    public function shortcode_handler($atts) {
        $atts = shortcode_atts([
            'title' => 'Default Title',
            'content' => 'Default Content'
        ], $atts);

        return sprintf(
            '<div class="my-shortcode"><h3>%s</h3><p>%s</p></div>',
            esc_html($atts['title']),
            esc_html($atts['content'])
        );
    }
}

// Initialize plugin
MyCustomPlugin::get_instance();
?>
