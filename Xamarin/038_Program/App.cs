using Xamarin.Forms;

namespace Program038
{
    public class App : Application
    {
        private int count = 0;
        private bool isChecked = false;
        private Label countLabel;
        private Label checkLabel;

        public App()
        {
            countLabel = new Label
            {
                Text = "Count: 0",
                FontSize = 20,
                HorizontalTextAlignment = TextAlignment.Center
            };

            checkLabel = new Label
            {
                Text = "Checked: False",
                FontSize = 20,
                HorizontalTextAlignment = TextAlignment.Center
            };

            MainPage = new ContentPage
            {
                Content = new StackLayout
                {
                    VerticalOptions = LayoutOptions.Center,
                    Spacing = 15,
                    Padding = 20,
                    Children =
                    {
                        new Label
                        {
                            Text = "State Demo 038",
                            FontSize = 28,
                            FontAttributes = FontAttributes.Bold,
                            HorizontalTextAlignment = TextAlignment.Center
                        },
                        countLabel,
                        new Button
                        {
                            Text = "Increment",
                            BackgroundColor = Color.FromHex("#2196F3"),
                            TextColor = Color.White,
                            Command = new Command(() =>
                            {
                                count++;
                                countLabel.Text = $"Count: {count}";
                            })
                        },
                        new Switch
                        {
                            HorizontalOptions = LayoutOptions.Center,
                            OnColor = Color.FromHex("#4CAF50")
                        }.Bind(Switch.IsToggledProperty, new Binding("IsChecked"))
                            .OnPropertyChanged((s, e) =>
                            {
                                if (e.PropertyName == "IsToggled")
                                {
                                    isChecked = (s as Switch).IsToggled;
                                    checkLabel.Text = $"Checked: {isChecked}";
                                }
                            }),
                        checkLabel
                    }
                }
            };
        }
    }
}
