namespace MyApp.Services
{
    public interface ISingletonService
    {
        Guid GetId();
    }

    public interface IScopedService
    {
        Guid GetId();
    }

    public interface ITransientService
    {
        Guid GetId();
    }

    public class SingletonService : ISingletonService
    {
        private readonly Guid _id = Guid.NewGuid();
        public Guid GetId() => _id;
    }

    public class ScopedService : IScopedService
    {
        private readonly Guid _id = Guid.NewGuid();
        public Guid GetId() => _id;
    }

    public class TransientService : ITransientService
    {
        private readonly Guid _id = Guid.NewGuid();
        public Guid GetId() => _id;
    }
}
