class JWTController < ApplicationController
  before_action :set_jwt, only: [:show, :edit, :update, :destroy]

  # GET /jwt
  def index
    @jwts = JWT.all
    render json: @jwts
  end

  # GET /jwt/1
  def show
    render json: @jwt
  end

  # POST /jwt
  def create
    @jwt = JWT.new(jwt_params)

    if @jwt.save
      render json: @jwt, status: :created
    else
      render json: @jwt.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /jwt/1
  def update
    if @jwt.update(jwt_params)
      render json: @jwt
    else
      render json: @jwt.errors, status: :unprocessable_entity
    end
  end

  # DELETE /jwt/1
  def destroy
    @jwt.destroy
    head :no_content
  end

  private

  def set_jwt
    @jwt = JWT.find(params[:id])
  end

  def jwt_params
    params.require(:jwt).permit(:name)
  end
end
