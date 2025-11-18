class ControllerController < ApplicationController
  before_action :set_controller, only: [:show, :edit, :update, :destroy]

  # GET /controller
  def index
    @controllers = Controller.all
    render json: @controllers
  end

  # GET /controller/1
  def show
    render json: @controller
  end

  # POST /controller
  def create
    @controller = Controller.new(controller_params)

    if @controller.save
      render json: @controller, status: :created
    else
      render json: @controller.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /controller/1
  def update
    if @controller.update(controller_params)
      render json: @controller
    else
      render json: @controller.errors, status: :unprocessable_entity
    end
  end

  # DELETE /controller/1
  def destroy
    @controller.destroy
    head :no_content
  end

  private

  def set_controller
    @controller = Controller.find(params[:id])
  end

  def controller_params
    params.require(:controller).permit(:name)
  end
end
