class DecoratorController < ApplicationController
  before_action :set_decorator, only: [:show, :edit, :update, :destroy]

  # GET /decorator
  def index
    @decorators = Decorator.all
    render json: @decorators
  end

  # GET /decorator/1
  def show
    render json: @decorator
  end

  # POST /decorator
  def create
    @decorator = Decorator.new(decorator_params)

    if @decorator.save
      render json: @decorator, status: :created
    else
      render json: @decorator.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /decorator/1
  def update
    if @decorator.update(decorator_params)
      render json: @decorator
    else
      render json: @decorator.errors, status: :unprocessable_entity
    end
  end

  # DELETE /decorator/1
  def destroy
    @decorator.destroy
    head :no_content
  end

  private

  def set_decorator
    @decorator = Decorator.find(params[:id])
  end

  def decorator_params
    params.require(:decorator).permit(:name)
  end
end
