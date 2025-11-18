class GuardController < ApplicationController
  before_action :set_guard, only: [:show, :edit, :update, :destroy]

  # GET /guard
  def index
    @guards = Guard.all
    render json: @guards
  end

  # GET /guard/1
  def show
    render json: @guard
  end

  # POST /guard
  def create
    @guard = Guard.new(guard_params)

    if @guard.save
      render json: @guard, status: :created
    else
      render json: @guard.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /guard/1
  def update
    if @guard.update(guard_params)
      render json: @guard
    else
      render json: @guard.errors, status: :unprocessable_entity
    end
  end

  # DELETE /guard/1
  def destroy
    @guard.destroy
    head :no_content
  end

  private

  def set_guard
    @guard = Guard.find(params[:id])
  end

  def guard_params
    params.require(:guard).permit(:name)
  end
end
