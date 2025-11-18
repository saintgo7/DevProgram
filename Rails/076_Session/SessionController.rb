class SessionController < ApplicationController
  before_action :set_session, only: [:show, :edit, :update, :destroy]

  # GET /session
  def index
    @sessions = Session.all
    render json: @sessions
  end

  # GET /session/1
  def show
    render json: @session
  end

  # POST /session
  def create
    @session = Session.new(session_params)

    if @session.save
      render json: @session, status: :created
    else
      render json: @session.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /session/1
  def update
    if @session.update(session_params)
      render json: @session
    else
      render json: @session.errors, status: :unprocessable_entity
    end
  end

  # DELETE /session/1
  def destroy
    @session.destroy
    head :no_content
  end

  private

  def set_session
    @session = Session.find(params[:id])
  end

  def session_params
    params.require(:session).permit(:name)
  end
end
