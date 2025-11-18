class MiddlewareController < ApplicationController
  before_action :set_middleware, only: [:show, :edit, :update, :destroy]

  # GET /middleware
  def index
    @middlewares = Middleware.all
    render json: @middlewares
  end

  # GET /middleware/1
  def show
    render json: @middleware
  end

  # POST /middleware
  def create
    @middleware = Middleware.new(middleware_params)

    if @middleware.save
      render json: @middleware, status: :created
    else
      render json: @middleware.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /middleware/1
  def update
    if @middleware.update(middleware_params)
      render json: @middleware
    else
      render json: @middleware.errors, status: :unprocessable_entity
    end
  end

  # DELETE /middleware/1
  def destroy
    @middleware.destroy
    head :no_content
  end

  private

  def set_middleware
    @middleware = Middleware.find(params[:id])
  end

  def middleware_params
    params.require(:middleware).permit(:name)
  end
end
