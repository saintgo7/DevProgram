class CookieController < ApplicationController
  before_action :set_cookie, only: [:show, :edit, :update, :destroy]

  # GET /cookie
  def index
    @cookies = Cookie.all
    render json: @cookies
  end

  # GET /cookie/1
  def show
    render json: @cookie
  end

  # POST /cookie
  def create
    @cookie = Cookie.new(cookie_params)

    if @cookie.save
      render json: @cookie, status: :created
    else
      render json: @cookie.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /cookie/1
  def update
    if @cookie.update(cookie_params)
      render json: @cookie
    else
      render json: @cookie.errors, status: :unprocessable_entity
    end
  end

  # DELETE /cookie/1
  def destroy
    @cookie.destroy
    head :no_content
  end

  private

  def set_cookie
    @cookie = Cookie.find(params[:id])
  end

  def cookie_params
    params.require(:cookie).permit(:name)
  end
end
