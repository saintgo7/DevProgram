using Xamarin.Forms;

namespace Program004
{
    public class App : Application
    {
        private Entry nameEntry;
        private Entry emailEntry;
        private Editor messageEditor;

        public App()
        {
            nameEntry = new Entry
            {
                Placeholder = "Name",
                Margin = new Thickness(10)
            };

            emailEntry = new Entry
            {
                Placeholder = "Email",
                Keyboard = Keyboard.Email,
                Margin = new Thickness(10)
            };

            messageEditor = new Editor
            {
                Placeholder = "Message",
                HeightRequest = 100,
                Margin = new Thickness(10)
            };

            var submitButton = new Button
            {
                Text = "Submit",
                BackgroundColor = Color.FromHex("#2196F3"),
                TextColor = Color.White,
                Margin = new Thickness(10),
                Command = new Command(async () =>
                {
                    if (!string.IsNullOrWhiteSpace(nameEntry.Text) &&
                        !string.IsNullOrWhiteSpace(emailEntry.Text))
                    {
                        await Application.Current.MainPage.DisplayAlert(
                            "Form Submitted",
                            $"Name: {nameEntry.Text}\nEmail: {emailEntry.Text}",
                            "OK"
                        );
                    }
                })
            };

            MainPage = new ContentPage
            {
                Title = "Form Demo",
                Content = new StackLayout
                {
                    Children =
                    {
                        new Label
                        {
                            Text = "Personal Information",
                            FontSize = 18,
                            FontAttributes = FontAttributes.Bold,
                            Margin = new Thickness(10, 10, 10, 5)
                        },
                        nameEntry,
                        emailEntry,
                        new Label
                        {
                            Text = "Message",
                            FontSize = 18,
                            FontAttributes = FontAttributes.Bold,
                            Margin = new Thickness(10, 10, 10, 5)
                        },
                        messageEditor,
                        submitButton
                    }
                }
            };
        }
    }
}
