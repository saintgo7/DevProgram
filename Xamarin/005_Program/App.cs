using Xamarin.Forms;

namespace Program005
{
    public class DetailPage : ContentPage
    {
        public DetailPage(string itemName)
        {
            Title = "Details";

            Content = new StackLayout
            {
                VerticalOptions = LayoutOptions.Center,
                HorizontalOptions = LayoutOptions.Center,
                Children =
                {
                    new Label
                    {
                        Text = itemName,
                        FontSize = 32,
                        FontAttributes = FontAttributes.Bold,
                        HorizontalTextAlignment = TextAlignment.Center
                    },
                    new Label
                    {
                        Text = "This is the detail page",
                        FontSize = 18,
                        TextColor = Color.Gray,
                        HorizontalTextAlignment = TextAlignment.Center,
                        Margin = new Thickness(0, 10, 0, 0)
                    }
                }
            };
        }
    }

    public class App : Application
    {
        public App()
        {
            var items = new[] { "Item 1", "Item 2", "Item 3", "Item 4", "Item 5" };

            var listView = new ListView
            {
                ItemsSource = items,
                ItemTemplate = new DataTemplate(() =>
                {
                    var label = new Label
                    {
                        VerticalOptions = LayoutOptions.Center,
                        Margin = new Thickness(10)
                    };
                    label.SetBinding(Label.TextProperty, ".");
                    return new ViewCell { View = label };
                })
            };

            listView.ItemSelected += async (sender, e) =>
            {
                if (e.SelectedItem != null)
                {
                    await (MainPage as NavigationPage)?.PushAsync(
                        new DetailPage(e.SelectedItem.ToString())
                    );
                    listView.SelectedItem = null;
                }
            };

            var mainPage = new ContentPage
            {
                Title = "Items",
                Content = listView
            };

            MainPage = new NavigationPage(mainPage);
        }
    }
}
