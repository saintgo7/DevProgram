class LikeController < ApplicationController
  before_action :set_like, only: [:show, :edit, :update, :destroy]

  # GET /like
  def index
    @likes = Like.all
    render json: @likes
  end

  # GET /like/1
  def show
    render json: @like
  end

  # POST /like
  def create
    @like = Like.new(like_params)

    if @like.save
      render json: @like, status: :created
    else
      render json: @like.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /like/1
  def update
    if @like.update(like_params)
      render json: @like
    else
      render json: @like.errors, status: :unprocessable_entity
    end
  end

  # DELETE /like/1
  def destroy
    @like.destroy
    head :no_content
  end

  private

  def set_like
    @like = Like.find(params[:id])
  end

  def like_params
    params.require(:like).permit(:name)
  end
end
