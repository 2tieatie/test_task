driver_options: tuple = ('--enable-features=NetworkService,NetworkServiceInProcess',
                          '--disable-features=VizDisplayCompositor',
                          '--disable-web-security',
                          '--allow-running-insecure-content',
                          '--disable-site-isolation-trials',
                          '--disable-notifications',
                          '--disable-translate',
                          '--disable-save-password-bubble',
                          '--disable-background-timer-throttling',
                          '--disable-backgrounding-occluded-windows',
                          '--disable-dev-shm-usage', '--no-sandbox',
                          '--remote-debugging-port=9222',
                          '--user-data-dir=/tmp/user-data',
                          '--data-path=/tmp/data-path',
                          '--homedir=/tmp',
                          '--disk-cache-dir=/tmp/cache-dir',
                          '--disable-software-rasterizer',
                          '--disable-dev-tools',
                          '--disable-logging',
                          '--log-level=3',
                          '--mute-audio',
                          '--disable-breakpad',
                          '--disable-ipc-flooding-protection',
                          '--disable-verify-client-certificates',
                          '--disable-wake-on-wifi',
                          '--enable-automation',
                          '--metrics-recording-only',
                          '--no-first-run')

query: str = 'developer'
pattern: str = f'https://www.linkedin.com/search/results/people/?keywords={query}'
wrong_results: tuple = ('https://www.linkedin.com/feed/?nis=true',
                       f'https://www.linkedin.com/search/results/people/headless?origin=OTHER&keywords={query}')
cont_inf_pattern: str = '/overlay/contact-info/'