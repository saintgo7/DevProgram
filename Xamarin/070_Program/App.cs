using Xamarin.Forms;

namespace Program070
{
    public class App : Application
    {
        public App()
        {
            var entry = new Entry
            {
                Placeholder = "Enter text",
                Margin = new Thickness(10)
            };

            var outputLabel = new Label
            {
                Text = "Text: ",
                FontSize = 18,
                Margin = new Thickness(10)
            };

            entry.TextChanged += (s, e) =>
            {
                outputLabel.Text = $"Text: {e.NewTextValue}";
            };

            var slider = new Slider
            {
                Minimum = 0,
                Maximum = 100,
                Value = 50,
                Margin = new Thickness(10)
            };

            var sliderLabel = new Label
            {
                Text = "Value: 50",
                FontSize = 18,
                Margin = new Thickness(10)
            };

            slider.ValueChanged += (s, e) =>
            {
                sliderLabel.Text = $"Value: {(int)e.NewValue}";
            };

            MainPage = new ContentPage
            {
                Title = "Input Demo 070",
                Content = new StackLayout
                {
                    Spacing = 10,
                    Children = { entry, outputLabel, slider, sliderLabel }
                }
            };
        }
    }
}
