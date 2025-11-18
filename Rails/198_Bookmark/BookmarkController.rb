class BookmarkController < ApplicationController
  before_action :set_bookmark, only: [:show, :edit, :update, :destroy]

  # GET /bookmark
  def index
    @bookmarks = Bookmark.all
    render json: @bookmarks
  end

  # GET /bookmark/1
  def show
    render json: @bookmark
  end

  # POST /bookmark
  def create
    @bookmark = Bookmark.new(bookmark_params)

    if @bookmark.save
      render json: @bookmark, status: :created
    else
      render json: @bookmark.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /bookmark/1
  def update
    if @bookmark.update(bookmark_params)
      render json: @bookmark
    else
      render json: @bookmark.errors, status: :unprocessable_entity
    end
  end

  # DELETE /bookmark/1
  def destroy
    @bookmark.destroy
    head :no_content
  end

  private

  def set_bookmark
    @bookmark = Bookmark.find(params[:id])
  end

  def bookmark_params
    params.require(:bookmark).permit(:name)
  end
end
