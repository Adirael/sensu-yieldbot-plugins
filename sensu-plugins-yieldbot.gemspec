lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)

require 'date'

if RUBY_VERSION < '2.0.0'
  require 'sensu-plugins-yieldbot'
else
  require_relative 'lib/sensu-plugins-yieldbot'
end

Gem::Specification.new do |s|
  librbfiles = File.join("bin/**", "*.rb")

  s.authors                = ['Anthony Spring']
  # s.executables            = Dir.glob(librbfiles).map { |file| File.basename(file) }
  # s.files                  = Dir.glob('{bin,lib}/**/*') + %w(LICENSE README.md CHANGELOG.md)

  s.name                   = 'sensu-plugins-yieldbot'
  s.platform               = Gem::Platform::RUBY
  s.post_install_message   = 'You can use the embedded Ruby by setting EMBEDDED_RUBY=true in /etc/default/sensu'
  s.require_paths          = ['lib']
  s.required_ruby_version  = '>= 2.1.0'
  s.summary                = 'Sensu plugins for Yieldbot'
  s.test_files             = s.files.grep(%r{^(test|spec|features)/})
  s.version                = SensuPluginsYieldbot::Version::VER_STRING

  s.add_runtime_dependency 'sensu-plugin',      '~> 4.0'

  s.add_development_dependency 'codeclimate-test-reporter', '~> 0.4'
  s.add_development_dependency 'rubocop',                   '0.49.0'
  s.add_development_dependency 'rspec',                     '~> 3.1'
  s.add_development_dependency 'bundler',                   '~> 2.1'
  s.add_development_dependency 'rake',                      '~> 10.0'
  s.add_development_dependency 'github-markup',             '~> 1.3'
  s.add_development_dependency 'redcarpet',                 '~> 3.2'
  s.add_development_dependency 'yard',                      '~> 0.9.11'
  s.add_development_dependency 'pry',                       '~> 0.10'
end
