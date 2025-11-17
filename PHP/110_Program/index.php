<?php
/**
 * WordPress Custom Post Type and Taxonomy
 */

// Register Custom Post Type
function register_book_post_type() {
    $labels = [
        'name'               => 'Books',
        'singular_name'      => 'Book',
        'menu_name'          => 'Books',
        'add_new'            => 'Add New Book',
        'add_new_item'       => 'Add New Book',
        'edit_item'          => 'Edit Book',
        'new_item'           => 'New Book',
        'view_item'          => 'View Book',
        'search_items'       => 'Search Books',
        'not_found'          => 'No books found',
        'not_found_in_trash' => 'No books found in trash',
    ];

    $args = [
        'labels'              => $labels,
        'public'              => true,
        'has_archive'         => true,
        'publicly_queryable'  => true,
        'query_var'           => true,
        'rewrite'             => ['slug' => 'books'],
        'capability_type'     => 'post',
        'hierarchical'        => false,
        'menu_icon'           => 'dashicons-book',
        'supports'            => ['title', 'editor', 'thumbnail', 'excerpt', 'custom-fields'],
        'show_in_rest'        => true, // Enable Gutenberg editor
    ];

    register_post_type('book', $args);
}
add_action('init', 'register_book_post_type');

// Register Custom Taxonomy
function register_book_taxonomy() {
    $labels = [
        'name'              => 'Genres',
        'singular_name'     => 'Genre',
        'search_items'      => 'Search Genres',
        'all_items'         => 'All Genres',
        'parent_item'       => 'Parent Genre',
        'parent_item_colon' => 'Parent Genre:',
        'edit_item'         => 'Edit Genre',
        'update_item'       => 'Update Genre',
        'add_new_item'      => 'Add New Genre',
        'new_item_name'     => 'New Genre Name',
        'menu_name'         => 'Genres',
    ];

    $args = [
        'labels'            => $labels,
        'hierarchical'      => true,
        'public'            => true,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => ['slug' => 'genre'],
        'show_in_rest'      => true,
    ];

    register_taxonomy('genre', ['book'], $args);
}
add_action('init', 'register_book_taxonomy');

// Add custom meta box
function add_book_meta_boxes() {
    add_meta_box(
        'book_details',
        'Book Details',
        'render_book_meta_box',
        'book',
        'normal',
        'high'
    );
}
add_action('add_meta_boxes', 'add_book_meta_boxes');

function render_book_meta_box($post) {
    wp_nonce_field('book_meta_box', 'book_meta_box_nonce');

    $author = get_post_meta($post->ID, '_book_author', true);
    $isbn = get_post_meta($post->ID, '_book_isbn', true);
    $price = get_post_meta($post->ID, '_book_price', true);
    ?>
    <p>
        <label for="book_author">Author:</label>
        <input type="text" id="book_author" name="book_author"
               value="<?php echo esc_attr($author); ?>" style="width: 100%;">
    </p>
    <p>
        <label for="book_isbn">ISBN:</label>
        <input type="text" id="book_isbn" name="book_isbn"
               value="<?php echo esc_attr($isbn); ?>" style="width: 100%;">
    </p>
    <p>
        <label for="book_price">Price:</label>
        <input type="number" id="book_price" name="book_price" step="0.01"
               value="<?php echo esc_attr($price); ?>">
    </p>
    <?php
}

// Save meta box data
function save_book_meta_box($post_id) {
    if (!isset($_POST['book_meta_box_nonce'])) {
        return;
    }

    if (!wp_verify_nonce($_POST['book_meta_box_nonce'], 'book_meta_box')) {
        return;
    }

    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    if (isset($_POST['book_author'])) {
        update_post_meta($post_id, '_book_author', sanitize_text_field($_POST['book_author']));
    }

    if (isset($_POST['book_isbn'])) {
        update_post_meta($post_id, '_book_isbn', sanitize_text_field($_POST['book_isbn']));
    }

    if (isset($_POST['book_price'])) {
        update_post_meta($post_id, '_book_price', sanitize_text_field($_POST['book_price']));
    }
}
add_action('save_post_book', 'save_book_meta_box');

// Custom query example
function get_recent_books($limit = 5) {
    $args = [
        'post_type'      => 'book',
        'posts_per_page' => $limit,
        'orderby'        => 'date',
        'order'          => 'DESC',
        'tax_query'      => [
            [
                'taxonomy' => 'genre',
                'field'    => 'slug',
                'terms'    => 'fiction',
            ],
        ],
    ];

    $query = new WP_Query($args);

    if ($query->have_posts()) {
        while ($query->have_posts()) {
            $query->the_post();
            // Display book
            the_title();
            the_excerpt();
        }
        wp_reset_postdata();
    }
}
?>
