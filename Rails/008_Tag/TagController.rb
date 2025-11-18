class TagController < ApplicationController
  before_action :set_tag, only: [:show, :edit, :update, :destroy]

  # GET /tag
  def index
    @tags = Tag.all
    render json: @tags
  end

  # GET /tag/1
  def show
    render json: @tag
  end

  # POST /tag
  def create
    @tag = Tag.new(tag_params)

    if @tag.save
      render json: @tag, status: :created
    else
      render json: @tag.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /tag/1
  def update
    if @tag.update(tag_params)
      render json: @tag
    else
      render json: @tag.errors, status: :unprocessable_entity
    end
  end

  # DELETE /tag/1
  def destroy
    @tag.destroy
    head :no_content
  end

  private

  def set_tag
    @tag = Tag.find(params[:id])
  end

  def tag_params
    params.require(:tag).permit(:name)
  end
end
