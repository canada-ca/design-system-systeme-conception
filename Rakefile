require "jekyll"

require "open3"

LANGUAGES = %w[en fr].freeze

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
  LANGUAGES.each do |language|
    build_language(language, "_site/#{language}", ["_config.yml"])
  end
end

desc "Build both preview language sites"
task :staging do
  abort "Set JEKYLL_ENV to staging." unless ENV["JEKYLL_ENV"] == "staging"

  pr_number = ENV.fetch("PR_NUMBER", "")
  abort "Set PR_NUMBER to a positive pull request number." unless pr_number.match?(/\A[1-9][0-9]*\z/)

  parser = File.expand_path(".github/scripts/parse_target.sh", __dir__)
  paths, status = Open3.capture2(
    "bash", "-c", 'source "$1" && parse_preview_target "$2" && printf "%s\n" "$EN_DIR" "$FR_DIR"',
    "parse_target", parser, ENV.fetch("PREVIEW_HOST_REPO", "")
  )
  abort "Set PREVIEW_HOST_REPO to a valid preview target." unless status.success?

  LANGUAGES.zip(paths.lines(chomp: true)).each do |language, path|
    build_language(
      language,
      "_staging/#{language}",
      ["_config.yml", "_config.staging.yml"],
      baseurl: "/#{path}/pr-preview/pr-#{pr_number}"
    )
  end
end
