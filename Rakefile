require "jekyll"

LANGUAGE_PATHS = {
  "en" => "design-system",
  "fr" => "systeme-conception"
}.freeze

def build_language(language, destination, config_files, baseurl: "")
  config = Jekyll.configuration(
    "source" => File.expand_path(language, __dir__),
    "destination" => File.expand_path(destination, __dir__),
    "config" => config_files.map { |file| File.expand_path(file, __dir__) },
    "safe" => true,
    "lang" => language,
    "baseurl" => baseurl
  )
  Jekyll::Site.new(config).process
end

desc "Build both production language sites"
task :build do
  ENV["JEKYLL_ENV"] = "production"
  LANGUAGE_PATHS.each_key do |language|
    build_language(language, "_site/#{language}", ["_config.yml"])
  end
end

desc "Build both preview language sites"
task :staging do
  abort "Set JEKYLL_ENV to staging." unless ENV["JEKYLL_ENV"] == "staging"

  pr_number = ENV.fetch("PR_NUMBER", "")
  abort "Set PR_NUMBER to a positive pull request number." unless pr_number.match?(/\A[1-9][0-9]*\z/)

  LANGUAGE_PATHS.each do |language, path|
    build_language(
      language,
      "_staging/#{path}/#{language}",
      ["_config.yml", "_config.staging.yml"],
      baseurl: "/#{path}/pr-preview/pr-#{pr_number}"
    )
  end
end
