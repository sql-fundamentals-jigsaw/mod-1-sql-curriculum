class Song < Person

  attr_reader :name
  # attr_writer :artist

  def artist=(artist)
    #
    @artist = artist

  end

  def initialize(name)
    @name = name
  end
end
