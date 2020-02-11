require 'rspec/core/rake_task'
require 'rubocop/rake_task'
require 'rdoc/task'

RSpec::Core::RakeTask.new(:spec) do |r|
  r.pattern = FileList['**/**/*_spec.rb']
end

RuboCop::RakeTask.new

Rake::RDocTask.new do |rd|
  rd.rdoc_dir = 'doc/rdocs'
  rd.rdoc_files.include "plugins/**/*\.rb"
  rd.options << '--line-numbers'
  rd.options << '--all'
end

desc 'Make all plugins executable'
task :make_plugins_executable do
  `chmod -R +x /plugins/*`
end

task default: [:spec, :rubocop]
