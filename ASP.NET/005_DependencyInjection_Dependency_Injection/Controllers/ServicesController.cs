using Microsoft.AspNetCore.Mvc;
using MyApp.Services;

namespace MyApp.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ServicesController : ControllerBase
    {
        private readonly ISingletonService _singleton;
        private readonly IScopedService _scoped;
        private readonly ITransientService _transient;

        public ServicesController(
            ISingletonService singleton,
            IScopedService scoped,
            ITransientService transient)
        {
            _singleton = singleton;
            _scoped = scoped;
            _transient = transient;
        }

        [HttpGet]
        public IActionResult GetServiceIds()
        {
            return Ok(new
            {
                Singleton = _singleton.GetId(),
                Scoped = _scoped.GetId(),
                Transient = _transient.GetId()
            });
        }
    }
}
