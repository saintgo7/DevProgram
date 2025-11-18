class FollowController < ApplicationController
  before_action :set_follow, only: [:show, :edit, :update, :destroy]

  # GET /follow
  def index
    @follows = Follow.all
    render json: @follows
  end

  # GET /follow/1
  def show
    render json: @follow
  end

  # POST /follow
  def create
    @follow = Follow.new(follow_params)

    if @follow.save
      render json: @follow, status: :created
    else
      render json: @follow.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /follow/1
  def update
    if @follow.update(follow_params)
      render json: @follow
    else
      render json: @follow.errors, status: :unprocessable_entity
    end
  end

  # DELETE /follow/1
  def destroy
    @follow.destroy
    head :no_content
  end

  private

  def set_follow
    @follow = Follow.find(params[:id])
  end

  def follow_params
    params.require(:follow).permit(:name)
  end
end
